# RUN: %PYTHON %s | FileCheck %s

import torch
import numpy as np

from mpact.mpactbackend import mpact_linalg

from mpact.models.kernels import MMNet


net = MMNet()

X = torch.arange(0, 16, dtype=torch.float32).view(4, 4)
Y = torch.arange(16, 32, dtype=torch.float32).view(4, 4)

#
# CHECK: module {
# CHECK:   func.func @main(%[[A0:.*]]: tensor<4x4xf32>, %[[A1:.*]]: tensor<4x4xf32>) -> tensor<4x4xf32> {
# CHECK:    %[[C0:.*]] = arith.constant 0.000000e+00 : f32
# CHECK:    %[[T0:.*]] = tensor.empty() : tensor<4x4xf32>
# CHECK:    %[[T1:.*]] = linalg.fill ins(%[[C0]] : f32) outs(%[[T0]] : tensor<4x4xf32>) -> tensor<4x4xf32>
# CHECK:    %[[T2:.*]] = linalg.matmul
# CHECK-SAME:              ins(%[[A0]], %[[A1]] : tensor<4x4xf32>, tensor<4x4xf32>)
# CHECK-SAME:              outs(%[[T1]] : tensor<4x4xf32>) -> tensor<4x4xf32>
# CHECK:    return %2 : tensor<4x4xf32>
# CHECK:   }
# CHECK: }
#

linalg = mpact_linalg(net, X, Y)
print(linalg)
