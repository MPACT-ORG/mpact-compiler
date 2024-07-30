import torch
import math
import numpy as np
from typing import Any


def generate_inputs(
    shapes: tuple[Any, ...],
    sparsity: float,
    formats: tuple[str, ...],
    dtype: Any = np.float64,
    drange: tuple[Any, ...] = (1, 100),
) -> tuple[tuple[torch.Tensor, ...], tuple[torch.Tensor, ...]]:
    """Generates dense and sparse tensor inputs.

    Args:
      shapes: Shape for each input.
      sparsity: Sparsity level for the inputs.
      formats: Sparsity format for each input.
      dtype: Data type of the generated inputs. Default is np.float64.
      drange: Data range of the non-zero values. Default is (1, 100).

    Returns:
      dense_inputs: all dense tensors.
      sparse_inputs: inputs are of the specified sparsity format, such as CSR.
    """
    dense_inputs = []
    sparse_inputs = []
    # Each input has a different seed.
    for seed, shape in enumerate(shapes):
        dense_inputs.append(generate_tensor(seed, shape, sparsity, dtype, drange))
    for idx, dense_input in enumerate(dense_inputs):
        if formats[idx] == "dense":
            sparse_inputs.append(dense_input)
        else:
            # TODO: support more sparsity formats.
            sparse_inputs.append(dense_input.to_sparse_csr())
    return dense_inputs, sparse_inputs


def generate_tensor(
    seed: int,
    shape: tuple[Any, ...],
    sparsity: float,
    dtype: Any = np.float64,
    drange: tuple[Any, ...] = (1, 100),
) -> torch.Tensor:
    """Generates a tensor given sparsity level, shape and data type.

    Args:
        seed: Seed value for np.random.
        shape: A tuple for the shape of tensor.
        sparsity: Sparsity level in the range of [0, 1], viz. 0=dense and 1=all-zeros
        dtype: Data type of the generated tensor. Default is np.float64.
        drange: Data range of the non-zero values (inclusive). Default is (1, 100).

    Returns:
        A dense torch tensor with the specified shape, sparsity level and type.

    Note: the tensor generated doesn't guarantee each batch will have the same
    number of specified elements. Therefore, for batched CSR, torch.cat can be
    used to concatenate generated tensors in the specified dimension.
    """
    if sparsity < 0.0 or sparsity > 1.0:
        raise ValueError("Invalid sparsity level: %f" % sparsity)

    np.random.seed(seed)
    size = math.prod(shape)
    nse = size - int(math.ceil(sparsity * size))

    flat_output = np.zeros(size)
    indices = np.random.choice(size, nse, replace=False)
    values = np.random.uniform(drange[0], drange[1], nse)
    flat_output[indices] = values

    result = np.reshape(flat_output, shape).astype(dtype)
    return torch.from_numpy(result)
