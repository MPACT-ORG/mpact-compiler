import pytest
from mpact.models.kernels import *
from mpact_benchmark.utils.tensor_generator import generate_tensor

SHAPE = (1024, 1024)
SPARSITY = 0.8

dense_tensor1 = generate_tensor(0, SHAPE, SPARSITY)
dense_tensor2 = generate_tensor(1, SHAPE, SPARSITY)
dense_tensor3 = generate_tensor(2, SHAPE, SPARSITY)
dense_vector = generate_tensor(1, (SHAPE[0],), SPARSITY)

temp = generate_tensor(0, (2046, 2046), 0.5)

sparse_tensor1 = dense_tensor1.to_sparse_csr()
sparse_tensor2 = dense_tensor2.to_sparse_csr()
sparse_tensor3 = dense_tensor3.to_sparse_csr()


def test_mv_dense(benchmark):
    benchmark(MVNet(), dense_tensor1, dense_vector)


def test_mm_dense(benchmark):
    benchmark(MMNet(), dense_tensor1, dense_tensor2)


def test_add_dense(benchmark):
    benchmark(AddNet(), dense_tensor1, dense_tensor2)


def test_mul_dense(benchmark):
    benchmark(MulNet(), dense_tensor1, dense_tensor2)


def test_nop_dense(benchmark):
    benchmark(SelfNet(), dense_tensor1)


def test_sddmm_dense(benchmark):
    benchmark(SDDMMNet(), temp, temp, temp)


def test_mv_sparse(benchmark):
    benchmark(MVNet(), sparse_tensor1, dense_vector)


def test_mm_sparse(benchmark):
    benchmark(MMNet(), sparse_tensor1, sparse_tensor2)


def test_add_sparse(benchmark):
    benchmark(AddNet(), sparse_tensor1, sparse_tensor2)


def test_mul_sparse(benchmark):
    benchmark(MulNet(), sparse_tensor1, sparse_tensor2)


def test_nop_sparse(benchmark):
    benchmark(SelfNet(), sparse_tensor1)


def test_sddmm_sparse(benchmark):
    benchmark(SDDMMNet(), temp, temp, temp)
