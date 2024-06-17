# RUN: %PYTHON %s | FileCheck %s

import torch
import numpy as np

from mpact.mpactbackend import mpact_jit, mpact_jit_compile, mpact_jit_run

from mpact.models.kernels import MMNet


def print_sparse(res):
    print(res[0])
    print(res[1])
    print(res[2])


net = MMNet()

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
# CHECK:   tensor({{\[}}[ 152.,  158.,  164.,  170.],
# CHECK:                [ 504.,  526.,  548.,  570.],
# CHECK:                [ 856.,  894.,  932.,  970.],
# CHECK:                [1208., 1262., 1316., 1370.]{{\]}})
# CHECK:  tensor({{\[}}[20., 21., 22., 23.],
# CHECK:               [56., 58., 60., 62.],
# CHECK:               [ 0.,  0.,  0.,  0.],
# CHECK:               [48., 51., 54., 57.]{{\]}})
# CHECK:  tensor({{\[}}[ 9.,  0.,  0.,  2.],
# CHECK:               [21.,  4.,  0., 10.],
# CHECK:               [33.,  8.,  0., 18.],
# CHECK:               [45., 12.,  0., 26.]{{\]}})
# CHECK:  tensor(crow_indices=tensor([0, 1, 2, 2, 3]),
# CHECK:         col_indices=tensor([3, 0, 1]),
# CHECK:         values=tensor([2., 6., 3.]), size=(4, 4), nnz=3,
# CHECK:         layout=torch.sparse_csr)
# CHECK: mpact
# CHECK:   {{\[}}[ 152.  158.  164.  170.]
# CHECK:         [ 504.  526.  548.  570.]
# CHECK:         [ 856.  894.  932.  970.]
# CHECK:         [1208. 1262. 1316. 1370.]{{\]}}
# CHECK:   {{\[}}[20. 21. 22. 23.]
# CHECK:         [56. 58. 60. 62.]
# CHECK:         [ 0.  0.  0.  0.]
# CHECK:         [48. 51. 54. 57.]{{\]}}
# CHECK:   {{\[}}[ 9.  0.  0.  2.]
# CHECK:         [21.  4.  0. 10.]
# CHECK:         [33.  8.  0. 18.]
# CHECK:         [45. 12.  0. 26.]{{\]}}
# CHECK:  [0 1 2 2 3]
# CHECK:  [3 0 1]
# CHECK:  [2. 6. 3.]
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
print(res)
res = mpact_jit(net, X, S)
print(res)
res = mpact_jit(net, S, S)
print_sparse(res)
