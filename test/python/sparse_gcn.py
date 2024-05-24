# RUN: %PYTHON %s | FileCheck %s

import torch

from mpact.mpactbackend import mpact_jit, mpact_jit_compile, mpact_jit_run
from mpact.models.gcn import GraphConv

net = GraphConv(4, 4)

# Get random (but reproducible) matrices.
torch.manual_seed(0)
inp = torch.rand(4, 4)
adj_mat = torch.rand(4, 4).to_sparse()

#
# CHECK: pytorch
# CHECK:   tensor({{\[}}[4.4778, 4.4778, 4.4778, 4.4778],
# CHECK:                [5.7502, 5.7502, 5.7502, 5.7502],
# CHECK:                [4.6980, 4.6980, 4.6980, 4.6980],
# CHECK:                [3.6407, 3.6407, 3.6407, 3.6407]{{\]}})
# CHECK: mpact compile and run
# CHECK:   {{\[}}[4.477828  4.477828  4.477828  4.477828 ]
# CHECK:         [5.7501717 5.7501717 5.7501717 5.7501717]
# CHECK:         [4.697952  4.697952  4.697952  4.697952 ]
# CHECK:         [3.640687  3.640687  3.640687  3.640687 ]{{\]}}
# CHECK: mpact compile
# CHECK: mpact run
# CHECK:   {{\[}}[4.477828  4.477828  4.477828  4.477828 ]
# CHECK:         [5.7501717 5.7501717 5.7501717 5.7501717]
# CHECK:         [4.697952  4.697952  4.697952  4.697952 ]
# CHECK:         [3.640687  3.640687  3.640687  3.640687 ]{{\]}}
#
with torch.no_grad():
    # Run it with PyTorch.
    print("pytorch")
    res = net(inp, adj_mat)
    print(res)

    # Run it with MPACT (compile and run at once).
    print("mpact compile and run")
    res = mpact_jit(net, inp, adj_mat)
    print(res)

    # Run it with MPACT (with separate compile and run steps).
    print("mpact compile")
    invoker, fn = mpact_jit_compile(net, inp, adj_mat)
    print("mpact run")
    res = mpact_jit_run(invoker, fn, inp, adj_mat)
    print(res)
