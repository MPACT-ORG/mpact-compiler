# RUN: %PYTHON %s | FileCheck %s

import torch
import numpy as np

from mpact.mpactbackend import mpact_jit, mpact_jit_compile, mpact_jit_run

from mpact.models.kernels import MMNet, SDDMMNet

mmnet = MMNet()
sddmmnet = SDDMMNet()

# Construct very sparse matrix.
idx = torch.tensor([[0, 4], [0, 4]], dtype=torch.int64)
val = torch.tensor([2.0, 3.0], dtype=torch.float64)
S = torch.sparse_coo_tensor(idx, val, size=[5, 5])

# Trivial dense inputs.
A = torch.arange(0, 25, dtype=torch.float32).view(5, 5)
B = torch.arange(25, 50, dtype=torch.float32).view(5, 5)

#
# CHECK: pytorch
# CHECK: tensor({{\[}}[ 400.,  410.,  420.,  430.,  440.],
# CHECK:              [1275., 1310., 1345., 1380., 1415.],
# CHECK:              [2150., 2210., 2270., 2330., 2390.],
# CHECK:              [3025., 3110., 3195., 3280., 3365.],
# CHECK:              [3900., 4010., 4120., 4230., 4340.]{{\]}})
# CHECK:   tensor(indices=tensor({{\[}}[0, 4],
# CHECK:                               [0, 4]{{\]}}),
# CHECK:          values=tensor([  800., 13020.]),
# CHECK:          size=(5, 5), nnz=2, dtype=torch.float64, layout=torch.sparse_coo)
# CHECK: mpact
# CHECK:   {{\[}}[ 400.  410.  420.  430.  440.]
# CHECK:         [1275. 1310. 1345. 1380. 1415.]
# CHECK:         [2150. 2210. 2270. 2330. 2390.]
# CHECK:         [3025. 3110. 3195. 3280. 3365.]
# CHECK:         [3900. 4010. 4120. 4230. 4340.]{{\]}}
# CHECK:   [0 2]
# CHECK:   [0 4]
# CHECK:   [0 4]
# CHECK:   [  800. 13020.]
#

# Run it with PyTorch.
print("pytorch")
dense = mmnet(A, B)
print(dense)
res = sddmmnet(S, A, B)
print(res)

# Run it with MPACT.
print("mpact")
dense = mpact_jit(mmnet, A, B)
print(dense)
res = mpact_jit(sddmmnet, S, A, B)
print(res[0])
print(res[1])
print(res[2])
print(res[3])
