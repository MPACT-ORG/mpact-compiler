# RUN: %PYTHON %s | FileCheck %s

import numpy as np

from mpact_benchmark.utils.tensor_generator import (
    generate_tensor,
    print_matrix_market_format,
    print_extended_frostt_format,
)

x = generate_tensor(
    seed=0, shape=(4, 7), sparsity=0.5, dtype=np.float32, drange=(4.0, 4.0)
)

# CHECK: %%MatrixMarket matrix coordinate real general
# CHECK: % https://math.nist.gov/MatrixMarket/formats.html
# CHECK: %
# CHECK: % density = 50.00%
# CHECK: %
# CHECK: 4 7 14
# CHECK: 1 2 4.0
# CHECK: 1 3 4.0
# CHECK: 1 6 4.0
# CHECK: 2 4 4.0
# CHECK: 2 5 4.0
# CHECK: 2 7 4.0
# CHECK: 3 1 4.0
# CHECK: 3 3 4.0
# CHECK: 3 4 4.0
# CHECK: 3 7 4.0
# CHECK: 4 2 4.0
# CHECK: 4 4 4.0
# CHECK: 4 5 4.0
# CHECK: 4 7 4.0
print_matrix_market_format(x)

# CHECK: # Tensor in Extended FROSTT file format
# CHECK: # http://frostt.io/tensors/file-formats.html
# CHECK: # extended with two metadata lines:
# CHECK: #   rank nnz
# CHECK: #   dims (one per rank)
# CHECK: #
# CHECK: # density = 50.00%
# CHECK: #
# CHECK: 2 14
# CHECK: 4 7
# CHECK: 1 2 4.0
# CHECK: 1 3 4.0
# CHECK: 1 6 4.0
# CHECK: 2 4 4.0
# CHECK: 2 5 4.0
# CHECK: 2 7 4.0
# CHECK: 3 1 4.0
# CHECK: 3 3 4.0
# CHECK: 3 4 4.0
# CHECK: 3 7 4.0
# CHECK: 4 2 4.0
# CHECK: 4 4 4.0
# CHECK: 4 5 4.0
# CHECK: 4 7 4.0
print_extended_frostt_format(x)
