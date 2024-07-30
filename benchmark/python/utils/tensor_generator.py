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


def print_matrix_market_format(tensor: torch.Tensor):
    """Prints the matrix market format for a sparse matrix.

    Args:
      tensor: sparse matrix (real type)
    """
    if len(tensor.shape) != 2:
        raise ValueError("Unexpected rank : %d (matrices only)" % len(tensor.shape))
    if tensor.dtype != torch.float32 and tensor.dtype != torch.float64:
        raise ValueError("Unexpected type : %s" % tensor.dtype)

    h = tensor.shape[0]
    w = tensor.shape[1]
    nnz = sum([1 if tensor[i, j] != 0 else 0 for i in range(h) for j in range(w)])
    density = (100.0 * nnz) / tensor.numel()
    print("%%MatrixMarket matrix coordinate real general")
    print("% https://math.nist.gov/MatrixMarket/formats.html")
    print("%")
    print("%% density = %4.2f%%" % density)
    print("%")
    print(h, w, nnz)
    for i in range(h):
        for j in range(w):
            if tensor[i, j] != 0:
                print(i + 1, j + 1, tensor[i, j].item())


def print_extended_frostt_format(tensor: torch.Tensor):
    """Prints the Extended FROSTT format for a sparse tensor.

    Args:
      tensor: sparse tensor
    """
    a = tensor.numpy()
    nnz = sum([1 if x != 0 else 0 for x in np.nditer(a)])
    density = (100.0 * nnz) / tensor.numel()
    print("# Tensor in Extended FROSTT file format")
    print("# http://frostt.io/tensors/file-formats.html")
    print("# extended with two metadata lines:")
    print("#   rank nnz")
    print("#   dims (one per rank)")
    print("#")
    print("# density = %4.2f%%" % density)
    print("#")
    print(len(tensor.shape), nnz)
    print(*tensor.shape, sep=" ")
    it = np.nditer(a, flags=["multi_index"])
    for x in it:
        if x != 0:
            print(*[i + 1 for i in it.multi_index], sep=" ", end=" ")
            print(x)
