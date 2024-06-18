# RUN: %PYTHON %s | FileCheck %s

import torch
import numpy as np

from mpact.mpactbackend import mpact_jit, mpact_jit_compile, mpact_jit_run

from mpact.models.gat import gat_4_64_8_3

net = gat_4_64_8_3()
net.eval()  # Switch to inference.

# Sparse input.
idx = torch.tensor([[0, 0, 1, 2], [0, 2, 3, 1]], dtype=torch.int64)
val = torch.tensor([14.0, 3.0, -8.0, 11.0], dtype=torch.float32)
S = torch.sparse_coo_tensor(idx, val, size=[4, 4])

# Construct adjacency matrix.
V = 4
edges = np.array([[0, 1], [0, 2], [1, 2], [1, 3], [2, 3]], dtype=np.int32)
E = edges.shape[0]
adj_mat = torch.sparse_coo_tensor(edges.T, torch.ones(E), (V, V), dtype=torch.int64)
adj_mat = (
    torch.eye(V) + adj_mat
)  # Add self-loops to the adjacency matrix (becomes dense)


#
# CHECK: pytorch gat
# CHECK:   tensor({{\[}}[-1.0986, -1.0986, -1.0986],
# CHECK:                [-1.0986, -1.0986, -1.0986],
# CHECK:                [-1.0986, -1.0986, -1.0986],
# CHECK:                [-1.0986, -1.0986, -1.0986]{{\]}}
# CHECK: mpact gat
# CHECK:   {{\[}}[-1.0986123 -1.0986123 -1.0986123]
# CHECK:         [-1.0986123 -1.0986123 -1.0986123]
# CHECK:         [-1.0986123 -1.0986123 -1.0986123]
# CHECK:         [-1.0986123 -1.0986123 -1.0986123]{{\]}}
#
with torch.no_grad():
    # Run it with PyTorch.
    print("pytorch gat")
    res = net(S, adj_mat)
    print(res)

    print("mpact gat")
    res = mpact_jit(net, S, adj_mat)
    print(res)
