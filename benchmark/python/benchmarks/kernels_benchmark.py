import torch
import argparse
import numpy as np
from mpact_benchmark.utils.benchmark_utils import benchmark, Backends


@benchmark(
    [
        {
            "name": f"{lhs_fmt}_{rhs_fmt}_{shape}_{dtype.__name__}",
            "shape": shape,
            "formats": (lhs_fmt, rhs_fmt),
            "dtype": dtype,
            "backends": [b for b in Backends],
            "drange": (1, 100),
            "sparsity": [0, 0.5, 0.9, 0.99],
        }
        for shape in [([2**i, 2**i], [2**i, 2**i]) for i in range(5, 8)]
        for lhs_fmt in ["dense", "csr"]
        for rhs_fmt in ["dense", "csr"]
        for dtype in [np.float64]
    ]
)
def matmul() -> torch.nn.Module:
    """Matrix multiplication."""

    class Net(torch.nn.Module):
        def __init__(self):
            super().__init__()

        def forward(self, x, y):
            return torch.matmul(x, y)

    return Net()


@benchmark(
    [
        {
            "name": f"{lhs_fmt}_{rhs_fmt}_{shape}_{dtype.__name__}",
            "shape": shape,
            "formats": (lhs_fmt, rhs_fmt),
            "dtype": dtype,
            "backends": [b for b in Backends],
            "drange": (1, 100),
            "sparsity": [0, 0.5, 0.9, 0.99],
        }
        for shape in [([2**i, 2**i], [2**i]) for i in range(5, 8)]
        for lhs_fmt in ["dense", "csr"]
        for rhs_fmt in ["dense"]  # torch.mv only supports dense vector for now.
        for dtype in [np.float64]
    ]
)
def matvec() -> torch.nn.Module:
    """Matrix-vector multiplication."""

    class Net(torch.nn.Module):
        def __init__(self):
            super().__init__()

        def forward(self, x, y):
            return torch.mv(x, y)

    return Net()


@benchmark(
    [
        {
            "name": f"{lhs_fmt}_{rhs_fmt}_{shape}_{dtype.__name__}",
            "shape": shape,
            "formats": (lhs_fmt, rhs_fmt),
            "dtype": dtype,
            "backends": [b for b in Backends],
            "drange": (1, 100),
            "sparsity": [0, 0.5, 0.9, 0.99],
        }
        for shape in [
            ([2**i, 2**i], [2**i, 2**i]) for i in range(5, 8)
        ]  # 512x512 crashes runtime.
        for lhs_fmt in ["dense", "csr"]
        for rhs_fmt in ["dense", "csr"]
        for dtype in [np.float64]
    ]
)
def add() -> torch.nn.Module:
    """Element-wise addition."""

    class Net(torch.nn.Module):
        def __init__(self):
            super().__init__()

        def forward(self, x, y):
            return torch.add(x, y)

    return Net()


@benchmark(
    [
        {
            "name": f"{lhs_fmt}_{rhs_fmt}_{shape}_{dtype.__name__}",
            "shape": shape,
            "formats": (lhs_fmt, rhs_fmt),
            "dtype": dtype,
            "backends": [b for b in Backends],
            "drange": (1, 100),
            "sparsity": [0, 0.5, 0.9, 0.99],
        }
        for shape in [([2**i, 2**i], [2**i, 2**i]) for i in range(5, 8)]
        for lhs_fmt in ["dense", "csr"]
        for rhs_fmt in ["dense", "csr"]
        for dtype in [np.float64]
    ]
)
def elt_mul() -> torch.nn.Module:
    """Element-wise addition."""

    class Net(torch.nn.Module):
        def __init__(self):
            super().__init__()

        def forward(self, x, y):
            return torch.mul(x, y)

    return Net()


@benchmark(
    [
        {
            "name": f"{fmt}_{shape}_{dtype.__name__}",
            "shape": shape,
            "formats": (fmt,),
            "dtype": dtype,
            "backends": [b for b in Backends],
            "drange": (1, 100),
            "sparsity": [0, 0.5, 0.9, 0.99],
        }
        for shape in [([2**i, 2**i],) for i in range(2, 3)]
        for fmt in ["dense", "csr"]
        for dtype in [np.float64]
    ]
)
def nop() -> torch.nn.Module:
    """Returns matrix unmodified (speed of light)."""

    class Net(torch.nn.Module):
        def __init__(self):
            super().__init__()

        def forward(self, x):
            return x

    return Net()


@benchmark(
    [
        {
            "name": f"{sample_fmt}_sample_{shape}_{dtype.__name__}",
            "shape": shape,
            "formats": (sample_fmt, "dense", "dense"),
            "dtype": dtype,
            "backends": [b for b in Backends],
            "drange": (1, 100),
            "sparsity": [0, 0.5, 0.9, 0.99],
        }
        for shape in [([2**i, 2**i], [2**i, 2**i], [2**i, 2**i]) for i in range(5, 8)]
        for sample_fmt in ["dense", "csr"]
        for dtype in [np.float64]
    ]
)
def sddmm() -> torch.nn.Module:
    """SDDMM: C = S ○ (A X B) Sampled dense-dense matrix-matrix multiplication."""

    class Net(torch.nn.Module):
        def __init__(self):
            super().__init__()

        def forward(self, x, y, z):
            return torch.mul(x, torch.matmul(y, z))

    return Net()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="pytorch_kernel_benchmarks",
        description="Run a set of given PyTorch kernel benchmarks",
    )
    parser.add_argument("--benchmark-filter", type=str, default="", required=False)
    arguments = parser.parse_args()

    benchmark_list = [
        "nop",
        "add",
        "matmul",
        "matvec",
        "elt_mul",
        "sddmm",
    ]
    if arguments.benchmark_filter:
        benchmark_list = arguments.benchmark_filter.split(",")

    # Run selected benchmarks.
    for benchmark_name in benchmark_list:
        globals()[benchmark_name]()
