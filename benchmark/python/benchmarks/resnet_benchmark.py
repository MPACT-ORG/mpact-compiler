import torch
import numpy as np
from mpact.models.resnet import resnet20
from mpact_benchmark.utils.benchmark_utils import benchmark, Backends


@benchmark(
    [
        {
            "name": f"{fmt}_{shape}_{dtype.__name__}",
            "shape": shape,
            "formats": fmt,
            "dtype": dtype,
            "drange": (1, 100),
            "sparsity": [0.5, 0.9],
            # TODO: Torch inductor requires lower precision with larger input size,
            # such as [8, 3, 32, 32].
            "precision": 1e-3,
            "backends": [b for b in Backends],
        }
        for shape in [
            [[1, 3, 16, 16]],
        ]
        for fmt in [["dense"]]
        for dtype in [np.float32]
    ]
)
def resnet() -> torch.nn.Module:
    """Restnet20 model."""
    resnet_model = resnet20()
    resnet_model.train(False)
    return resnet_model


if __name__ == "__main__":
    resnet()
