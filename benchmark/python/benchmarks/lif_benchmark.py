import torch
import numpy as np
from mpact.models.lif import Block
from mpact_benchmark.utils.benchmark_utils import benchmark, Backends


@benchmark(
    [
        {
            "name": f"{fmt}_{shape}_{dtype.__name__}",
            "shape": shape,
            "formats": [fmt],
            "dtype": dtype,
            # Simulate batch normalization.
            "drange": (-1, 1),
            "sparsity": [0, 0.5, 0.9, 0.99],
            # to_dense() in LIF prop hack is not supported in torch inductor.
            # TODO: add torch inductor once prop hack is no longer needed.
            "backends": [
                b
                for b in Backends
                if b.value
                not in (
                    Backends.TORCH_SPARSE_INDUCTOR.value,
                    Backends.TORCH_DENSE_INDUCTOR.value,
                )
            ],
        }
        for shape in [
            [[64, 3, 32, 32, 1]],
            [[32, 3, 64, 64, 1]],
            [[16, 3, 224, 224, 1]],
        ]
        for fmt in ["dense"]
        for dtype in [np.float64]
    ]
)
def SNN() -> torch.nn.Module:
    """Spiking Neural Network."""
    return Block


if __name__ == "__main__":
    SNN()
