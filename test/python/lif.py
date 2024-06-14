# RUN: %PYTHON %s | FileCheck %s

import torch

from mpact.mpactbackend import mpact_jit, mpact_jit_compile, mpact_jit_run

from mpact.models.lif import Block

net = Block()

# Get a random (but reproducible) input, so that a
# general sparse tensor appears after LIF.
torch.manual_seed(0)
x = torch.rand(2, 3, 8, 8)

#
# CHECK: pytorch
# CHECK:   tensor([ 0., 11.,  9., 11., 13., 11., 10., 12.])
# CHECK: mpact
# CHECK:   [ 0. 11.  9. 11. 13. 11. 10. 12.]
#

# Run it with PyTorch.
print("pytorch")
res = net(x)
print(res)

# Run it with MPACT.
print("mpact")
res = mpact_jit(net, x)
print(res)
