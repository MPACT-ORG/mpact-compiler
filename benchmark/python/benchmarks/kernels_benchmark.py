import torch
import argparse
import numpy as np
from mpact.models.kernels import *
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
    return MMNet()


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
    return MVNet()


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
    return AddNet()


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
    return MulNet()


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
    return SelfNet()


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
        for shape in [
            ([2**i, 2**i], [2**i, 2**i], [2**i, 2**i]) for i in range(5, 8)
        ]
        for sample_fmt in ["dense", "csr"]
        for dtype in [np.float64]
    ]
)
def sddmm() -> torch.nn.Module:
    """SDDMM: C = S ○ (A X B) Sampled dense-dense matrix-matrix multiplication."""
    return SDDMMNet()


@benchmark(
    [
        {
            "name": f"{fmt}_{shape}_{dtype.__name__}",
            "shape": shape,
            "formats": (fmt,),
            "dtype": dtype,
            # TODO: add mpact and torch inductor once they work.
            "backends": [
                b
                for b in Backends
                if b.value
                in (
                    Backends.TORCH_SPARSE_EAGER.value,
                    Backends.TORCH_DENSE_EAGER.value,
                )
            ],
            "drange": (1, 100),
            "sparsity": [0, 0.5, 0.9, 0.99],
        }
        for shape in [([2**i, 2**i],) for i in range(5, 8)]
        for fmt in ["dense"]
        for dtype in [np.float64]
    ]
)
def feature_scale() -> torch.nn.Module:
    """Scales feature matrix in GNN."""
    return FeatureScale()


@benchmark(
    [
        {
            "name": f"{fmt}_{shape}_{dtype.__name__}",
            "shape": shape,
            "formats": (fmt,),
            "dtype": dtype,
            # TODO: add mpact and torch inductor once they work.
            "backends": [
                b
                for b in Backends
                if b.value
                in (
                    Backends.TORCH_SPARSE_EAGER.value,
                    Backends.TORCH_DENSE_EAGER.value,
                )
            ],
            "drange": (1, 100),
            "sparsity": [0, 0.5, 0.9, 0.99],
        }
        for shape in [([2**i, 2**i],) for i in range(5, 8)]
        for fmt in ["dense"]
        for dtype in [np.float64]
    ]
)
def normalization() -> torch.nn.Module:
    """Normalizes adjacency matrix in GNN."""
    return Normalization()


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
        "feature_scale",
        "normalization",
    ]
    if arguments.benchmark_filter:
        benchmark_list = arguments.benchmark_filter.split(",")

    # Run selected benchmarks.
    for benchmark_name in benchmark_list:
        globals()[benchmark_name]()
