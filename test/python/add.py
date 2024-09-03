# RUN: %PYTHON %s | FileCheck %s

import torch
import numpy as np

from mpact.mpactbackend import mpact_jit

from mpact.models.kernels import AddNet


def print_sparse(res):
    print(res[0])
    print(res[1])
    print(res[2])


net = AddNet()

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
# CHECK:   tensor({{\[}}[16., 18., 20., 22.],
# CHECK:                [24., 26., 28., 30.],
# CHECK:                [32., 34., 36., 38.],
# CHECK:                [40., 42., 44., 46.]{{\]}})
# CHECK:  tensor({{\[}}[16., 18., 18., 19.],
# CHECK:               [20., 21., 22., 25.],
# CHECK:               [24., 25., 26., 27.],
# CHECK:               [31., 29., 30., 31.]{{\]}})
# CHECK:  tensor({{\[}}[ 0.,  2.,  2.,  3.],
# CHECK:               [ 4.,  5.,  6.,  9.],
# CHECK:               [ 8.,  9., 10., 11.],
# CHECK:               [15., 13., 14., 15.]{{\]}})
# CHECK:  tensor(crow_indices=tensor([0, 1, 2, 2, 3]),
# CHECK:         col_indices=tensor([1, 3, 0]),
# CHECK:         values=tensor([2., 4., 6.]), size=(4, 4), nnz=3,
# CHECK:         layout=torch.sparse_csr)
# CHECK: mpact
# CHECK:   {{\[}}[16. 18. 20. 22.]
# CHECK:         [24. 26. 28. 30.]
# CHECK:         [32. 34. 36. 38.]
# CHECK:         [40. 42. 44. 46.]{{\]}}
# CHECK:   {{\[}}[16. 18. 18. 19.]
# CHECK:         [20. 21. 22. 25.]
# CHECK:         [24. 25. 26. 27.]
# CHECK:         [31. 29. 30. 31.]{{\]}}
# CHECK:   {{\[}}[ 0.  2.  2.  3.]
# CHECK:         [ 4.  5.  6.  9.]
# CHECK:         [ 8.  9. 10. 11.]
# CHECK:         [15. 13. 14. 15.]{{\]}}
# CHECK:  [0 1 2 2 3]
# CHECK:  [1 3 0]
# CHECK:  [2. 4. 6.]
#

# Run it with PyTorch.
print("pytorch", torch.__version__)
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
