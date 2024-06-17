import torch
import numpy as np
from mpact.models.gcn import GraphConv
from mpact_benchmark.utils.benchmark_utils import benchmark, Backends


@benchmark(
    [
        {
            "name": f"{fmt}_{shape}_{dtype.__name__}",
            "shape": shape,
            "formats": fmt,
            "dtype": dtype,
            "drange": (1, 100),
            "sparsity": [0, 0.5, 0.9, 0.99],
            "backends": [b for b in Backends],
        }
        for shape in [
            [[128, 128], [128, 128]],
            [[512, 512], [512, 512]],
            [[1024, 1024], [1024, 1024]],
        ]
        for fmt in [["dense", "csr"]]
        for dtype in [np.float32]
    ]
)
def GCN() -> torch.nn.Module:
    """Graph Convolution Network."""
    return GraphConv


if __name__ == "__main__":
    GCN()
