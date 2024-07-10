# RUN: %PYTHON %s | FileCheck %s

import torch
import numpy as np

from mpact.mpactbackend import mpact_jit

from mpact.models.kernels import SqSum

net = SqSum()

# Construct adjacency matrix.
V = 8
edges = np.array([[0, 1], [0, 4], [1, 4], [3, 4], [4, 3]], dtype=np.int32)
E = edges.shape[0]
adj_mat = torch.sparse_coo_tensor(edges.T, torch.ones(E), (V, V), dtype=torch.int64)

#
# CHECK: pytorch
# CHECK:   tensor(5)
# CHECK: mpact
# CHECK:   5

# Run it with PyTorch.
print("pytorch")
res = net(adj_mat)
print(res)

# Run it with MPACT.
print("mpact")
# Try sparsification with sparse iterator
# TODO: will work after explicit value is specified in the encoding.
# res = mpact_jit(net, adj_mat, use_sp_it=True)
# print(res)
# Try sparsification directly with scf.for/while
res = mpact_jit(net, adj_mat)
print(res)
