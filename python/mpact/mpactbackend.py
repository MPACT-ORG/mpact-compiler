# Initialize mpact python extension.
import mpact._mlir_libs._mpact

import ctypes
from io import StringIO
import numpy as np
import os
import sys
import tempfile
import torch

from typing import Any, Callable, Optional, Tuple, Dict, TypeVar, Union

from mpact import ir
from mpact.ir import Module
from mpact.dialects import torch as torch_d
from mpact.execution_engine import *
from mpact.extras.fx_decomp_util import get_decomposition_table
from mpact.extras.fx_importer import FxImporter
from mpact.ir import *
from mpact.passmanager import *
from mpact.runtime import *

# One time set up of support library.
SUPPORT_LIB = os.getenv("SUPPORT_LIB", default=None)
SHARED_LIBS = [] if SUPPORT_LIB is None else [SUPPORT_LIB]

# The result of MPACT compile() and input to load().
MpactCompiledArtifact = TypeVar("MpactCompiledArtifact")


def get_module_name_for_debug_dump(module):
    """Gets a name suitable for a debug dump.

    The name is not guaranteed to be unique.
    """
    if not "torch.debug_module_name" in module.operation.attributes:
        return "UnnammedModule"
    return StringAttr(module.operation.attributes["torch.debug_module_name"]).value


class MPACTCompilerError(Exception):
    pass


def run_pipeline_with_repro_report(
    module, pipeline: str, description: str, enable_ir_printing: bool = False
):
    """Runs `pipeline` on `module`, with a nice repro report if it fails."""
    module_name = get_module_name_for_debug_dump(module)
    original_stderr = sys.stderr
    try:
        sys.stderr = StringIO()
        asm_for_error_report = module.operation.get_asm(
            large_elements_limit=10, enable_debug_info=True
        )
        # Lower module in place to make it ready for compiler backends.
        with module.context as ctx:
            pm = PassManager.parse(pipeline)
            if enable_ir_printing:
                ctx.enable_multithreading(False)
                pm.enable_ir_printing()
            pm.run(module.operation)
    except Exception as e:
        filename = os.path.join(tempfile.gettempdir(), module_name + ".mlir")
        with open(filename, "w") as f:
            f.write(asm_for_error_report)
        debug_options = "-mlir-print-ir-after-all -mlir-disable-threading"
        # Put something descriptive here even if description is empty.
        description = description or f"{module_name} compile"

        message = f"""\
            {description} failed with the following diagnostics:
            {sys.stderr.getvalue()}

            python exception: {e}

            The error can be reproduced with:
            $ mpact-opt -pass-pipeline='{pipeline}' {filename}
            Add '{debug_options}' to get the IR dump for debugging purpose.
            """
        trimmed_message = "\n".join([m.lstrip() for m in message.split("\n")])
        raise MPACTCompilerError(trimmed_message) from None
    finally:
        sys.stderr = original_stderr


def assert_arg_type_is_supported(ty):
    SUPPORTED = [
        np.float16,
        np.float32,
        np.float64,
        np.uint8,
        np.int8,
        np.int32,
        np.int64,
        np.bool_,
        np.complex64,
        np.complex128,
    ]
    assert (
        ty in SUPPORTED
    ), f"Only numpy arrays with dtypes in {SUPPORTED} are supported, but got {ty}"


memref_type_to_np_dtype = {
    "mrf16": np.float16,
    "mrf32": np.float32,
    "mrf64": np.float64,
    "mri1": np.bool_,
    "mri8": np.int8,
    "mri32": np.int32,
    "mri64": np.int64,
    "mrc32": np.complex64,
    "mrc64": np.complex128,
}
elemental_type_to_ctype = {
    "i1": ctypes.c_bool,
    "i8": ctypes.c_byte,
    "i64": ctypes.c_int,
    "f32": ctypes.c_float,
    "f64": ctypes.c_double,
}

CONSUME_RETURN_FUNC_PREFIX = "refbackend_consume_func_return_"


def get_return_funcs(module):
    return_prefix_len = len(CONSUME_RETURN_FUNC_PREFIX)
    return_funcs = []
    with module.context:
        for func in module.body:
            # Returns strings of the form `"refbackend.."` so `"` is deleted.
            func_name = str(func.attributes["sym_name"]).replace('"', "")
            if func_name[:return_prefix_len] == CONSUME_RETURN_FUNC_PREFIX:
                return_funcs.append(func_name)

    return return_funcs


def get_ctype_func(func_name):
    return_prefix_len = len(CONSUME_RETURN_FUNC_PREFIX)
    ret_types = func_name[return_prefix_len:].split("_")
    ctypes_arg = [None]
    for type in ret_types:
        if type in elemental_type_to_ctype:
            ctypes_arg.append(elemental_type_to_ctype[type])
        elif type in memref_type_to_np_dtype:
            ctypes_arg.append(ctypes.POINTER(UnrankedMemRefDescriptor))
        else:
            assert False, f"Not supported type: {type}"

    return ctypes.CFUNCTYPE(*ctypes_arg), ret_types


class MpactBackendInvoker:
    def __init__(self, module, opt_level):
        self.ee = ExecutionEngine(module, opt_level=opt_level, shared_libs=SHARED_LIBS)
        self.result = None

        return_funcs = get_return_funcs(module)

        for ret_func in return_funcs:
            ctype_wrapper, ret_types = get_ctype_func(ret_func)

            def consume_return_funcs(*args):
                self.result = tuple(
                    [
                        (
                            arg
                            if type in elemental_type_to_ctype
                            else unranked_memref_to_numpy(
                                arg, memref_type_to_np_dtype[type]
                            )
                        )
                        for arg, type in zip(args, ret_types)
                    ]
                )
                if len(self.result) == 1:
                    self.result = self.result[0]

            self.ee.register_runtime(ret_func, ctype_wrapper(consume_return_funcs))

    def __getattr__(self, function_name: str):
        def invoke(*args):
            ffi_args = []
            for arg in args:
                assert_arg_type_is_supported(arg.dtype)
                ffi_args.append(
                    ctypes.pointer(ctypes.pointer(get_unranked_memref_descriptor(arg)))
                )

            self.ee.invoke(function_name, *ffi_args)
            result = self.result
            assert result is not None, "Invocation didn't produce a result"
            self.result = None
            return result

        return invoke


LOWERING_PIPELINE_TEMPLATE = (
    "builtin.module("
    + ",".join(
        [
            "func.func(linalg-generalize-named-ops)",
            # Run pre-sparsification pass to fuse convert/cast op into
            # producer as they might hinder kernel fusions.
            "pre-sparsification-rewrite",
            "func.func(linalg-fuse-elementwise-ops)",
            "convert-shape-to-std",
            # Propagate sparse encodings before sparsifier mini-pipeline.
            # TODO: the following pass currently contains no pattern. Will be
            # added as needed.
            "func.func(sparse-encoding-propagation)",
            # MLIR Sparsifier mini-pipeline:
            #   use the PyTorch assembler conventions
            #   enable vectorization with VL=16 (more or less assumes AVX512 for float)
            #   allow 32-bit index optimizations (unsafe for very large dimensions)
            "sparse-assembler{{direct-out}}",
            "sparsification-and-bufferization{{{sp_options}}}",
            "sparse-storage-specifier-to-llvm",
            # Buffer deallocation pass does not know how to handle realloc.
            "func.func(expand-realloc)",
            # Generalize pad and concat after sparse compiler, as they are handled
            # differently when the operations involve sparse operands.
            "func.func(refback-generalize-tensor-pad)",
            "func.func(refback-generalize-tensor-concat)",
            # Bufferize.
            "func.func(tm-tensor-bufferize)",
            "one-shot-bufferize{{copy-before-write bufferize-function-boundaries function-boundary-type-conversion=identity-layout-map}}",
            "refback-mlprogram-bufferize",
            "func.func(finalizing-bufferize)",
            "func.func(buffer-deallocation)",
            # Inline sparse helper methods where useful (but after dealloc).
            "inline",
            "refback-munge-calling-conventions",
            "func.func(tm-tensor-to-loops)",
            "func.func(refback-munge-memref-copy)",
            "func.func(convert-linalg-to-loops)",
            "func.func(lower-affine)",
            "convert-scf-to-cf",
            "func.func(refback-expand-ops-for-llvm)",
            "func.func(arith-expand)",
            "func.func(convert-math-to-llvm)",
            "convert-math-to-libm",
            "expand-strided-metadata",
            "finalize-memref-to-llvm",
            "lower-affine",
            "convert-bufferization-to-memref",
            "finalize-memref-to-llvm",
            "func.func(convert-arith-to-llvm)",
            # Vector code (SIMD):
            #   allow fp reductions to reassociate
            #   allow 32-bit index optimizations (unsafe for very large dimensions)
            #   assume we are running on a good ol' Intel X86 (disable for ARM/other)
            "convert-vector-to-llvm{{reassociate-fp-reductions force-32bit-vector-indices enable-x86vector}}",
            "convert-func-to-llvm",
            "convert-cf-to-llvm",
            "convert-complex-to-llvm",
            "reconcile-unrealized-casts",
        ]
    )
    + ")"
)


class MpactBackendCompiler:
    """Main entry-point for the MPACT backend compiler."""

    def __init__(self, opt_level, use_sp_it):
        self.opt_level = opt_level
        self.use_sp_it = use_sp_it

    def compile(self, imported_module: Module) -> MpactCompiledArtifact:
        sp_options = (
            "sparse-emit-strategy=sparse-iterator"
            if self.use_sp_it
            else "vl=16 enable-simd-index32"
        )
        LOWERING_PIPELINE = LOWERING_PIPELINE_TEMPLATE.format(sp_options=sp_options)
        """Compiles an imported module, with a flat list of functions.
        The module is expected to be in linalg-on-tensors + scalar code form.

        Args:
          imported_module: The MLIR module in the torch dialect.
        Returns:
          An opaque artifact that can be passed to `load`.
        """
        run_pipeline_with_repro_report(
            imported_module,
            LOWERING_PIPELINE,
            "Lowering Linalg-on-Tensors IR to LLVM with MpactBackendCompiler",
            enable_ir_printing=False,
        )
        return imported_module

    def load(self, module: MpactCompiledArtifact) -> MpactBackendInvoker:
        """Loads a compiled artifact into the runtime.

        Args:
          module: The result of a previous call to `compile`.
        Returns:
          MPactInvoker to call a compiled method (viz `invoker.foo(...)`).
        """
        return MpactBackendInvoker(module, self.opt_level)


def export_and_import(f, *args, **kwargs):
    """A FX graph importer, stripped down to essentials."""
    context = ir.Context()
    torch_d.register_dialect(context)
    fx_importer = FxImporter(context=context)
    prog = torch.export.export(f, args, kwargs)
    decomposition_table = get_decomposition_table()
    if decomposition_table:
        prog = prog.run_decompositions(decomposition_table)
    fx_importer.import_frozen_program(prog)
    return fx_importer.module


def mpact_linalg(f, *args, **kwargs):
    """Imports a function as module and lowers it into Linalg IR."""
    module = export_and_import(f, *args, **kwargs)
    run_pipeline_with_repro_report(
        module,
        (
            "builtin.module("
            "func.func(torch-decompose-complex-ops),"
            "torch-backend-to-linalg-on-tensors-backend-pipeline)"
        ),
        "Lowering TorchFX IR -> Linalg IR",
        enable_ir_printing=False,
    )
    return module


def mpact_jit_compile(f, *args, opt_level=2, use_sp_it=False, **kwargs):
    """This method compiles the given callable using the MPACT backend."""
    module = mpact_linalg(f, *args, **kwargs)
    backend = MpactBackendCompiler(opt_level=opt_level, use_sp_it=use_sp_it)
    compiled = backend.compile(module)
    invoker = backend.load(compiled)
    return invoker, f


def mpact_jit_run(invoker, f, *args, **kwargs):
    """This method runs the given callable using the given MPACT invoker."""
    xargs = []
    # Prepare all the named buffer parameters (assume all dense).
    # All scalar arguments are filtered out since they appear inline.
    params = dict(f.named_buffers(remove_duplicate=True))
    params_flat, params_spec = torch.utils._pytree.tree_flatten(params)
    for p in params_flat:
        if len(p.shape) > 0:
            xargs.append(p.numpy())
    # Prepare input parameters. Sparse input tensors are split into
    # their composite tensors. All PyTorch tensors are converted
    # to their backing numpy arrays. Note that the output consists
    # of numpy arrays as well, which can trivially be reconstructed
    # into PyTorch tensors (dense and sparse).
    for a in args:
        if a.layout is torch.sparse_coo:
            # Construct the additional position array required by MLIR with data
            # array([0, nnz]). The COO format always uses int64 indices.
            xargs.append(np.array([0, a._nnz()], dtype=np.int64))
            # Transform a tensor<ndim x nnz> into ndim x tensor<nnz> to conform
            # to the MLIR SoA COO representation.
            for idx in a._indices():
                xargs.append(idx.numpy())
            xargs.append(a._values().numpy())
        elif a.layout is torch.sparse_csr or a.layout is torch.sparse_bsr:
            xargs.append(a.crow_indices().numpy())
            xargs.append(a.col_indices().numpy())
            xargs.append(a.values().numpy())
        elif a.layout is torch.sparse_csc or a.layout is torch.sparse_bsc:
            xargs.append(a.ccol_indices().numpy())
            xargs.append(a.row_indices().numpy())
            xargs.append(a.values().numpy())
        else:
            xargs.append(a.numpy())
    # Invoke.
    return invoker.main(*xargs)


# Convenience wrapper.
def mpact_jit(f, *args, **kwargs):
    """This method compiles and runs the given callable using the MPACT backend."""
    invoker, fn = mpact_jit_compile(f, *args, **kwargs)
    return mpact_jit_run(invoker, fn, *args, **kwargs)
