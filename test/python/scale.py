# RUN: %PYTHON %s | FileCheck %s

import torch
import numpy as np

from mpact.mpactbackend import mpact_jit

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
#
# TODO: first row?
#
# CHECK: mpact
# CHECK:   {{\[}}[0.         0.         0.         0.         0.         0.
# CHECK:          0.        ]
# CHECK:         [0.30635384 0.15570773 0.21608633 0.11923195 0.13728413 0.00762967
# CHECK:          0.05770639]
# CHECK:         [0.08555716 0.15095268 0.20310582 0.23290026 0.04687909 0.08217437
# CHECK:          0.19843069]
# CHECK:         [0.22065267 0.09574053 0.2107584  0.10111907 0.13330552 0.22970453
# CHECK:          0.00871931]
# CHECK:         [0.07743214 0.15609969 0.12754099 0.3896042  0.07353575 0.11279855
# CHECK:          0.06298868]
# CHECK:         [0.00931544 0.06112389 0.2730649  0.2123639  0.21801054 0.15456341
# CHECK:          0.07155795]
# CHECK:         [0.20259099 0.01148908 0.04807246 0.08394676 0.28260148 0.2748705
# CHECK:          0.09642864]]
#

# Run it with PyTorch.
print("pytorch")
res = net(features)
print(res)

# Run it with MPACT.
print("mpact")
res = mpact_jit(net, features)
print(res)
