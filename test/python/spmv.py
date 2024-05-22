# RUN: %PYTHON %s | FileCheck %s

import torch

from mpactbackend import mpact_jit, mpact_jit_compile, mpact_jit_run

class SpMVNet(torch.nn.Module):
    def forward(self, x, v):
        return torch.mv(x, v)

net = SpMVNet()

# Get a fixed vector and matrix (which we make 2x2 block "sparse").
dense_vector = torch.arange(1, 11, dtype=torch.float32)
dense_input = torch.arange(1, 101, dtype=torch.float32).view(10, 10)
sparse_matrix = dense_input.to_sparse_bsr(blocksize=(2, 2))

#
# CHECK: pytorch
# CHECK:   tensor([ 385.,  935., 1485., 2035., 2585., 3135., 3685., 4235., 4785., 5335.])
# CHECK: mpact
# CHECK:   [ 385.  935. 1485. 2035. 2585. 3135. 3685. 4235. 4785. 5335.]
#

# Run it with PyTorch.
print("pytorch")
res = net(sparse_matrix, dense_vector)
print(res)

# Run it with MPACT.
print("mpact")
res = mpact_jit(net, sparse_matrix, dense_vector)
print(res)
