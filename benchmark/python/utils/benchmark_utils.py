import functools
import torch
from enum import Enum
from typing import Any, Callable
from torch.utils import benchmark as torch_benchmark
from mpact.mpactbackend import mpact_jit, mpact_jit_compile, mpact_jit_run
from mpact_benchmark.utils.tensor_generator import generate_inputs


class Backends(Enum):
    TORCH_SPARSE_EAGER = 1
    TORCH_DENSE_EAGER = 2
    TORCH_SPARSE_INDUCTOR = 3
    TORCH_DENSE_INDUCTOR = 4
    MPACT_SPARSE = 5
    MPACT_DENSE = 6


def timer(stmt: str, description: str, setup: str = "", **kwargs: Any) -> Any:
    """Timer for benchmark."""
    return torch_benchmark.Timer(
        stmt=stmt,
        globals=kwargs["variables"],
        setup=setup,
        num_threads=1,
        label=kwargs["variables"]["label"],
        sub_label=kwargs["variables"]["sub_label"],
        description=description,
    ).adaptive_autorange()


def get_dynamo_compile_time(sub_label: str, label: str, description: str) -> Any:
    """Get compile time from dynamo and create a benchmark measurement object."""
    try:
        compile_time = torch_benchmark.Measurement(
            1,
            [
                float(
                    torch._dynamo.utils.compile_times(repr="csv")[1][0]
                    .split(",")[-1]
                    .strip()
                )
            ],
            torch_benchmark.TaskSpec(
                sub_label,
                None,
                description=description,
                label=label,
            ),
        )
        return compile_time
    except ValueError:
        print(f"No compilation happened for {description}: {sub_label}.")
        return None


def run_benchmark(
    sparse_inputs: tuple[torch.Tensor, ...],
    dense_inputs: tuple[torch.Tensor, ...],
    torch_net: torch.nn.Module,
    variables: dict[str, Any],
    backends: tuple[Backends, ...],
    runtime_results: list[torch_benchmark.Measurement],
    compile_time_results: list[torch_benchmark.Measurement],
):
    """Run benchmark with specified backends."""
    output = []
    output_type = None

    with torch.no_grad():
        for backend in backends:
            match backend:
                case Backends.TORCH_SPARSE_EAGER:
                    sparse_out = torch_net(*sparse_inputs)
                    output_type = sparse_out.layout
                    output.append(sparse_out)
                    runtime_results.append(
                        timer(
                            "torch_net(*sparse_inputs)",
                            "torch-sparse-eager",
                            variables=variables,
                        )
                    )
                case Backends.TORCH_DENSE_EAGER:
                    output.append(torch_net(*dense_inputs))
                    runtime_results.append(
                        timer(
                            "torch_net(*dense_inputs)",
                            "torch-dense-eager",
                            variables=variables,
                        )
                    )
                case Backends.TORCH_SPARSE_INDUCTOR:
                    torch_inductor = torch.compile(torch_net)
                    torch_out = torch_inductor(*sparse_inputs)
                    output.append(torch_out)
                    compile_time = get_dynamo_compile_time(
                        variables["sub_label"],
                        variables["label"],
                        "torch-sparse-inductor-compile",
                    )
                    if compile_time:
                        compile_time_results.append(compile_time)
                    runtime_results.append(
                        timer(
                            "torch_inductor(*sparse_inputs)",
                            "torch-sparse-inductor-runtime",
                            variables=dict(variables, **locals()),
                        )
                    )
                case Backends.TORCH_DENSE_INDUCTOR:
                    torch_inductor = torch.compile(torch_net)
                    output.append(torch_inductor(*dense_inputs))
                    compile_time = get_dynamo_compile_time(
                        variables["sub_label"],
                        variables["label"],
                        "torch-dense-inductor-compile",
                    )
                    if compile_time:
                        compile_time_results.append(compile_time)
                    runtime_results.append(
                        timer(
                            "torch_inductor(*dense_inputs)",
                            "torch-dense-inductor-runtime",
                            variables=dict(variables, **locals()),
                        )
                    )
                case Backends.MPACT_SPARSE:
                    sp_out = mpact_jit(torch_net, *sparse_inputs)
                    # Construct sparse csr tensor if the output type is csr.
                    # TODO: return sparse tensor directly instead of a tuple of arrays.
                    if type(sp_out) is tuple:
                        # torch.sparse_csr_tensor could deduce the size incorrectly,
                        # so pass the dense_out's shape explicitly.
                        dense_out = mpact_jit(torch_net, *dense_inputs)
                        output.append(
                            torch.sparse_csr_tensor(*sp_out, size=dense_out.shape)
                        )
                        # Check MPACT and torch eager both return sparse csr output.
                        if output_type:
                            assert output_type == torch.sparse_csr
                    else:
                        output.append(torch.from_numpy(sp_out))
                        # Check MPACT and torch eager both return dense output.
                        if output_type:
                            assert output_type == torch.strided
                    invoker, f = mpact_jit_compile(torch_net, *sparse_inputs)
                    compile_time_results.append(
                        timer(
                            "mpact_jit_compile(torch_net, *sparse_inputs)",
                            "mpact-sparse-compile",
                            "from mpact.mpactbackend import mpact_jit_compile",
                            variables=dict(variables, **locals()),
                        )
                    )
                    runtime_results.append(
                        timer(
                            "mpact_jit_run(invoker, f, *sparse_inputs)",
                            "mpact-sparse-runtime",
                            "from mpact.mpactbackend import mpact_jit_run",
                            variables=dict(variables, **locals()),
                        )
                    )
                case Backends.MPACT_DENSE:
                    output.append(torch.from_numpy(mpact_jit(torch_net, *dense_inputs)))
                    invoker, f = mpact_jit_compile(torch_net, *dense_inputs)
                    compile_time_results.append(
                        timer(
                            "mpact_jit_compile(torch_net, *dense_inputs)",
                            "mpact-dense-compile",
                            "from mpact.mpactbackend import mpact_jit_compile",
                            variables=dict(variables, **locals()),
                        )
                    )
                    runtime_results.append(
                        timer(
                            "mpact_jit_run(invoker, f, *dense_inputs)",
                            "mpact-dense-runtime",
                            "from mpact.mpactbackend import mpact_jit_run",
                            variables=dict(variables, **locals()),
                        )
                    )
                case _:
                    print(f"{backend} is not supported yet.")

    # Sanity check.
    if output:
        rtol = variables["precision"] if "precision" in variables else 1e-5
        assert all(
            torch.allclose(output[0].to_dense(), out.to_dense(), rtol=rtol)
            for out in output
        )


def benchmark(*args: Any) -> Callable:
    """Wrapper for benchmark."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(test_cases=args[0]):
            runtime_results = []
            compile_time_results = []
            torch_net = net = func()
            for test_case in test_cases:
                label = func.__name__
                for sparsity in test_case["sparsity"]:
                    sub_label = f"{test_case['name']}_{sparsity}"
                    dense_inputs, sparse_inputs = generate_inputs(
                        test_case["shape"],
                        sparsity,
                        test_case["formats"],
                        test_case["dtype"],
                        test_case["drange"],
                    )

                    if "GCN" in label:
                        torch_net = net(*test_case["shape"][0])
                    if "precision" in test_case:
                        precision = test_case["precision"]

                    run_benchmark(
                        sparse_inputs,
                        dense_inputs,
                        torch_net,
                        locals(),
                        test_case["backends"],
                        runtime_results,
                        compile_time_results,
                    )

            compare1 = torch_benchmark.Compare(runtime_results)
            compare1.print()
            compare2 = torch_benchmark.Compare(compile_time_results)
            compare2.print()

            return func

        return wrapper

    return decorator
