# RUN: %PYTHON %s | FileCheck %s

import torch
import numpy as np

from mpact.mpactbackend import mpact_jit, mpact_jit_compile, mpact_jit_run

from mpact.models.kernels import FeatureScale

net = FeatureScale()

# Get random (but reproducible) matrices.
torch.manual_seed(0)
features = torch.rand(7, 7)

#
# CHECK: pytorch
# CHECK:   tensor({{\[}}[0.1702, 0.2634, 0.0303, 0.0453, 0.1054, 0.2174, 0.1680],
# CHECK:                [0.3064, 0.1557, 0.2161, 0.1192, 0.1373, 0.0076, 0.0577],
# CHECK:                [0.0856, 0.1510, 0.2031, 0.2329, 0.0469, 0.0822, 0.1984],
# CHECK:                [0.2207, 0.0957, 0.2108, 0.1011, 0.1333, 0.2297, 0.0087],
# CHECK:                [0.0774, 0.1561, 0.1275, 0.3896, 0.0735, 0.1128, 0.0630],
# CHECK:                [0.0093, 0.0611, 0.2731, 0.2124, 0.2180, 0.1546, 0.0716],
# CHECK:                [0.2026, 0.0115, 0.0481, 0.0839, 0.2826, 0.2749, 0.0964]{{\]}})
# CHECK: mpact
#

# Run it with PyTorch.
print("pytorch")
res = net(features)
print(res)

# Run it with MPACT.
#
# TODO: make this work, crashes in TORCH-MLIR
#
print("mpact")
# res = mpact_jit(net, features)
# print(res)
