# RUN: %PYTHON %s | FileCheck %s

import torch
import numpy as np

from mpact.mpactbackend import mpact_jit

from mpact.models.kernels import CountEq


net = CountEq()

# Construct dense and sparse matrices.
A = torch.tensor(
    [
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 2.0],
        [0.0, 0.0, 1.0, 1.0],
        [3.0, 0.0, 3.0, 0.0],
    ],
    dtype=torch.float32,
)

# TODO: very interesting idiom to sparsify (collapse the sum
#       into the eq for full sparsity), but needs PyTorch support
S = A
# S = A.to_sparse()
# S = A.to_sparse_csr()

#
# CHECK: pytorch
# CHECK:  10
# CHECK:  3
# CHECK:  1
# CHECK:  2
# CHECK:  0
# CHECK: mpact
# CHECK:  10
# CHECK:  3
# CHECK:  1
# CHECK:  2
# CHECK:  0
#

# Run it with PyTorch.
print("pytorch")
for i in range(5):
    target = torch.tensor(i)
    res = net(S, target).item()
    print(res)

print("mpact")
for i in range(5):
    target = torch.tensor(i)
    res = mpact_jit(net, S, target)
    print(res)
