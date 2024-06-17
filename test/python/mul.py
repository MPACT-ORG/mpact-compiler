# RUN: %PYTHON %s | FileCheck %s

import torch
import numpy as np

from mpact.mpactbackend import mpact_jit, mpact_jit_compile, mpact_jit_run

from mpact.models.kernels import MulNet


def print_sparse(res):
    print(res[0])
    print(res[1])
    print(res[2])


net = MulNet()

# Construct dense and sparse matrices.
X = torch.arange(0, 16, dtype=torch.float32).view(4, 4)
Y = torch.arange(16, 32, dtype=torch.float32).view(4, 4)
A = torch.tensor(
    [
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 2.0],
        [0.0, 0.0, 0.0, 0.0],
        [3.0, 0.0, 0.0, 0.0],
    ],
    dtype=torch.float32,
)
S = A.to_sparse_csr()

#
# CHECK: pytorch
# CHECK: tensor({{\[}}[  0.,  17.,  36.,  57.],
# CHECK:              [ 80., 105., 132., 161.],
# CHECK:              [192., 225., 260., 297.],
# CHECK:              [336., 377., 420., 465.]{{\]}})
# CHECK: tensor(crow_indices=tensor([0, 1, 2, 2, 3]),
# CHECK:        col_indices=tensor([1, 3, 0]),
# CHECK:        values=tensor([17., 46., 84.]), size=(4, 4), nnz=3,
# CHECK:        layout=torch.sparse_csr)
# CHECK: tensor(crow_indices=tensor([0, 1, 2, 2, 3]),
# CHECK:        col_indices=tensor([1, 3, 0]),
# CHECK:        values=tensor([ 1., 14., 36.]), size=(4, 4), nnz=3,
# CHECK:        layout=torch.sparse_csr)
# CHECK: tensor(crow_indices=tensor([0, 1, 2, 2, 3]),
# CHECK:        col_indices=tensor([1, 3, 0]),
# CHECK:        values=tensor([1., 4., 9.]), size=(4, 4), nnz=3,
# CHECK:        layout=torch.sparse_csr)
# CHECK: mpact
# CHECK:   {{\[}}[  0.  17.  36.  57.]
# CHECK:         [ 80. 105. 132. 161.]
# CHECK:         [192. 225. 260. 297.]
# CHECK:         [336. 377. 420. 465.]{{\]}}
# CHECK:  [0 1 2 2 3]
# CHECK:  [1 3 0]
# CHECK:  [17. 46. 84.]
# CHECK:  [0 1 2 2 3]
# CHECK:  [1 3 0]
# CHECK:  [ 1. 14. 36.]
# CHECK:  [0 1 2 2 3]
# CHECK:  [1 3 0]
# CHECK:  [1. 4. 9.]
#

# Run it with PyTorch.
print("pytorch")
res = net(X, Y)
print(res)
res = net(S, Y)
print(res)
res = net(X, S)
print(res)
res = net(S, S)
print(res)

# Run it with MPACT.
print("mpact")
res = mpact_jit(net, X, Y)
print(res)
res = mpact_jit(net, S, Y)
print_sparse(res)
res = mpact_jit(net, X, S)
print_sparse(res)
res = mpact_jit(net, S, S)
print_sparse(res)
