# RUN: %PYTHON -s %s 2>&1 | FileCheck %s

import gc
import sys
import torch
import numpy as np

from mpact.mpactbackend import mpact_jit

from mpact.models.kernels import MMNet


def run_test(f, *args, **kwargs):
    print("TEST:", f.__name__, file=sys.stderr)
    f(*args, **kwargs)
    gc.collect()

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

# Run it with MPACT.
# TODO: enable the check test.
# C-HECK: omp.parallel
# CHECK: openmp
run_test(mpact_jit, net, X, Y,
         parallel="any-storage-any-loop", enable_ir_printing=True,
         num_threads=10)
