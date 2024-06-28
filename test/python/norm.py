# RUN: %PYTHON %s | FileCheck %s

import torch
import numpy as np

from mpact.mpactbackend import mpact_jit, mpact_jit_compile, mpact_jit_run

from mpact.models.kernels import Normalization

net = Normalization()

# Construct adjacency matrix.
V = 8
edges = np.array([[0, 1], [0, 4], [1, 4], [3, 4], [4, 3]], dtype=np.int32)
E = edges.shape[0]
adj_mat = torch.sparse_coo_tensor(edges.T, torch.ones(E), (V, V), dtype=torch.int64)
adj_mat = (
    torch.eye(V) + adj_mat
)  # Add self-loops to the adjacency matrix (becomes dense)

#
# CHECK: pytorch
# CHECK:   tensor({{\[}}[0.1111, 0.1667, 0.0000, 0.0000, 0.1667, 0.0000, 0.0000, 0.0000],
# CHECK:                [0.0000, 0.2500, 0.0000, 0.0000, 0.2500, 0.0000, 0.0000, 0.0000],
# CHECK:                [0.0000, 0.0000, 1.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
# CHECK:                [0.0000, 0.0000, 0.0000, 0.2500, 0.2500, 0.0000, 0.0000, 0.0000],
# CHECK:                [0.0000, 0.0000, 0.0000, 0.2500, 0.2500, 0.0000, 0.0000, 0.0000],
# CHECK:                [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 1.0000, 0.0000, 0.0000],
# CHECK:                [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 1.0000, 0.0000],
# CHECK:                [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 1.0000]{{\]}})
#
# TODO: first row?
#
# CHECK: mpact
# CHECK:   {{\[}}[0.   0.   0.   0.   0.   0.   0.   0.  ]
# CHECK:         [0.   0.25 0.   0.   0.25 0.   0.   0.  ]
# CHECK:         [0.   0.   1.   0.   0.   0.   0.   0.  ]
# CHECK:         [0.   0.   0.   0.25 0.25 0.   0.   0.  ]
# CHECK:         [0.   0.   0.   0.25 0.25 0.   0.   0.  ]
# CHECK:         [0.   0.   0.   0.   0.   1.   0.   0.  ]
# CHECK:         [0.   0.   0.   0.   0.   0.   1.   0.  ]
# CHECK:         [0.   0.   0.   0.   0.   0.   0.   1.  ]{{\]}}
#

# Run it with PyTorch.
print("pytorch")
res = net(adj_mat)
print(res)

# Run it with MPACT.
print("mpact")
res = mpact_jit(net, adj_mat)
print(res)
