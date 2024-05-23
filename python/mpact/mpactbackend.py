import ctypes
import numpy as np
import torch

from typing import Any, Callable, Optional, Tuple, Dict

from torch_mlir import ir
from torch_mlir.compiler_utils import run_pipeline_with_repro_report
from torch_mlir.dialects import torch as torch_d
from torch_mlir.execution_engine import *
from torch_mlir.extras.fx_importer import FxImporter, SparsityMeta
from torch_mlir.ir import *
from torch_mlir.passmanager import *
from torch_mlir.runtime import *

from torch_mlir_e2e_test.linalg_on_tensors_backends.refbackend import (
    LinalgOnTensorsBackend,
)

a = [  ]

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

SPARSE_LAYOUTS = [
    torch.sparse_coo,
    torch.sparse_csr,
    torch.sparse_csc,
    torch.sparse_bsr,
    torch.sparse_bsc,
]


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
    def __init__(self, module, opt_level=2, shared_libs=[]):
        self.ee = ExecutionEngine(module, opt_level=opt_level, shared_libs=shared_libs)
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


LOWERING_PIPELINE = (
    "builtin.module("
    + ",".join(
        [
            "func.func(linalg-generalize-named-ops)",
            "func.func(linalg-fuse-elementwise-ops)",
            "convert-shape-to-std",
            # MLIR Sparsifier mini-pipeline.
            "sparse-assembler{direct-out}",
            "sparsification-and-bufferization",
            "sparse-storage-specifier-to-llvm",
            # Buffer deallocation pass does not know how to handle realloc.
            "func.func(expand-realloc)",
            # Generalize pad and concat after sparse compiler, as they are handled
            # differently when the operations involve sparse operands.
            "func.func(refback-generalize-tensor-pad)",
            "func.func(refback-generalize-tensor-concat)",
            # Bufferize.
            "func.func(scf-bufferize)",
            "func.func(tm-tensor-bufferize)",
            "func.func(empty-tensor-to-alloc-tensor)",
            "func.func(linalg-bufferize)",
            "func-bufferize",
            "arith-bufferize",
            "refback-mlprogram-bufferize",
            "func.func(tensor-bufferize)",
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
            "convert-vector-to-llvm",
            "convert-func-to-llvm",
            "convert-cf-to-llvm",
            "convert-complex-to-llvm",
            "reconcile-unrealized-casts",
        ]
    )
    + ")"
)


class MpactBackendLinalgOnTensorsBackend(LinalgOnTensorsBackend):
    """Main entry-point for the MPACT backend."""

    def __init__(self):
        super().__init__()

    def compile(self, imported_module: Module):
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
            "Lowering Linalg-on-Tensors IR to LLVM with MpactBackend",
            enable_ir_printing=False,
        )
        return imported_module

    def load(self, module) -> MpactBackendInvoker:
        """Loads a compiled artifact into the runtime."""
        return MpactBackendInvoker(module)


def sparse_metadata(a: torch.Tensor) -> SparsityMeta:
    """
    Returns a meta data tuple for the given sparse tensor.

    NOTE: this will be fully replaced by fx graph SparseTensorMetadata
    """
    sparse_dim = a.sparse_dim()
    dense_dim = a.dense_dim()
    batch_dim = a.ndim - dense_dim - sparse_dim
    blocksize = None
    if a.layout is torch.sparse_coo:
        return SparsityMeta(
            a.layout,
            batch_dim,
            sparse_dim,
            dense_dim,
            blocksize,
            a._indices().dtype,
            a._indices().dtype,
        )
    elif a.layout is torch.sparse_csr or a.layout is torch.sparse_bsr:
        if a.layout is torch.sparse_bsr:
            blocksize = a.values().shape[batch_dim + 1 : batch_dim + 3]
        return SparsityMeta(
            a.layout,
            batch_dim,
            sparse_dim,
            dense_dim,
            blocksize,
            a.crow_indices().dtype,
            a.col_indices().dtype,
        )
    elif a.layout is torch.sparse_csc or a.layout is torch.sparse_bsc:
        if a.layout is torch.sparse_bsc:
            blocksize = a.values().shape[batch_dim + 1 : batch_dim + 3]
        return SparsityMeta(
            a.layout,
            batch_dim,
            sparse_dim,
            dense_dim,
            blocksize,
            a.ccol_indices().dtype,
            a.row_indices().dtype,
        )
    else:
        raise RuntimeError(f"Unsupported sparse layout for {a}")


def sparse_export(
    f: Callable, args: Tuple[Any, ...], kwargs: Optional[Dict[str, Any]] = None
) -> torch.export.ExportedProgram:
    """
    This is a ***temporary*** wrapper around `torch.export.export`
    that eventually should be removed and simply replaced by the
    standard API for exporting traced graphs.

    But until issue

      https://github.com/pytorch/pytorch/pull/117907

    is addressed, this wrapper provides support for the sparse
    tensor types by first converting all operands to dense tensors,
    building the traced graph as for the dense case, then annotating
    sparse parameters with their actual sparse layout attributes,
    followed by some simple propagation rules. This temporary solution
    accelerates testing torch-mlir with PyTorch sparse tensors until
    the issue is resolved upstream.
    """
    # Convert all arguments to dense.
    dargs = tuple(a.to_dense() if a.layout in SPARSE_LAYOUTS else a for a in args)
    mask = [a.layout in SPARSE_LAYOUTS for a in args]
    # Build the regular FX traced graph with only dense arguments
    # (the current version would crash otherwise, see issue above).
    prog = torch.export.export(f, dargs, kwargs)
    # Annotate sparse arguments in the graph and apply some very
    # basic propagation rules for sparsity.
    specs = prog.graph_signature.input_specs
    alen = len(specs)
    k = 0
    for i, node in enumerate(prog.graph.nodes):
        if node.op == "placeholder":
            # Argument.
            spec = specs[i]
            if spec.kind is torch.export.graph_signature.InputKind.USER_INPUT:
                if mask[k]:
                    node.meta["sparsity"] = sparse_metadata(args[k])
                k = k + 1
        elif node.op == "call_function":
            # TODO: use upstream _opname implementation when available
            opname = node.target._schema.name.split("::")[1]
            # Zero preserving elt-wise unary op.
            if opname in {"abs", "neg", "relu", "sin"}:
                node.meta["sparsity"] = node.args[0].meta.get("sparsity", None)
            elif opname == "_to_sparse":
                dim = len(node.meta.get("val").shape)
                node.meta["sparsity"] = SparsityMeta(
                    torch.sparse_coo, 0, dim, 0, None, torch.int64, torch.int64
                )
            # TODO: Uncomment this to hack sparsity into the network.
            # elif opname == "_to_dense":
            #     # hack (assumes we never really want the to_dense for now)
            #     node.meta["sparsity"] = node.args[0].meta.get("sparsity", None)
            elif opname == "select" and node.args[0].meta.get("sparsity", None):
                dim = len(node.meta.get("val").shape)
                node.meta["sparsity"] = SparsityMeta(
                    torch.sparse_coo, 0, dim, 0, None, torch.int64, torch.int64
                )
            elif opname == "stack" and node.args[0][0].meta.get("sparsity", None):
                dim = len(node.meta.get("val").shape)
                node.meta["sparsity"] = SparsityMeta(
                    torch.sparse_coo, 0, dim - 1, 1, None, torch.int64, torch.int64
                )
    return prog


def export_and_import(f, *args, **kwargs):
    """This method implements Stella's importer, stripped down to essentials."""
    context = ir.Context()
    torch_d.register_dialect(context)
    fx_importer = FxImporter(context=context)
    prog = sparse_export(f, args, kwargs)
    fx_importer.import_frozen_program(prog)
    return fx_importer.module


def mpact_jit_compile(f, *args, **kwargs):
    """This method compiles the given callable using the MPACT backend."""
    # Import module and lower into Linalg IR.
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
    # Compile with MPACT backend.
    backend = MpactBackendLinalgOnTensorsBackend()
    compiled = backend.compile(module)
    invoker = backend.load(compiled)
    return invoker, f


def mpact_jit_run(invoker, f, *args, **kwargs):
    """This method runs the given callable using the given MPACT invoker."""
    xargs = []
    # Prepare the buffer parameters (assume all dense).
    # TODO: filters out scalar arguments, anything else?
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


def mpact_jit(f, *args, **kwargs):
    """This method compiles and runs the given callable using the MPACT backend."""
    invoker, fn = mpact_jit_compile(f, *args, **kwargs)
    return mpact_jit_run(invoker, fn, *args, **kwargs)
