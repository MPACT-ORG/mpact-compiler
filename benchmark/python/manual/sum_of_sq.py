import torch
import numpy as np
import time

from mpact.mpactbackend import mpact_jit_compile, mpact_jit_run
from mpact_benchmark.utils.tensor_generator import generate_tensor


def runbench_eager(tag, sp, net, x, num_iters=1000):
    net(x)  # warmup
    checksum = 0
    start = time.time()
    for i in range(num_iters):
        res = net(x).item()
        checksum = checksum + res
    end = time.time()
    time_ms = (end - start) * 1000 / num_iters
    # print("%s : %.2f : %8.4f ms. : checksum=%d" % (tag, sp, time_ms, checksum))
    print(time_ms)


def runbench_mpact(tag, sp, net, x, num_iters=1000):
    invoker, fn = mpact_jit_compile(net, x)
    mpact_jit_run(invoker, fn, x)  # warmup
    checksum = 0
    start = time.time()
    for i in range(num_iters):
        res = mpact_jit_run(invoker, fn, x)
        checksum = checksum + res
    end = time.time()
    time_ms = (end - start) * 1000 / num_iters
    # print("%s : %.2f : %8.4f ms. : checksum=%d" % (tag, sp, time_ms, checksum))
    print(time_ms)


class SqSumNet(torch.nn.Module):
    def forward(self, x):
        # TODO: make this work too: return (x ** 2).sum()
        return (x * x).sum()


net = SqSumNet()
h = 1024 * 4
w = 1024 * 4

for d in range(0, 101, 10):
    sparsity = 1.0 - (d / 100.0)
    x = generate_tensor(
        seed=0, shape=(h, w), sparsity=sparsity, dtype=np.float32, drange=(1.0, 1.0)
    )

    # Note, we don't have binary-valued sparse tensors in PyTorch
    # so we are using csr. For now, we have to hack the
    #    "explicitVal=1.0:f32"
    # into the MLIR sparse tensor type to make optimize it fully.
    s = x.to_sparse_csr()

    # runbench_eager("PyTorch (dense) ", sparsity, net, x)
    # runbench_mpact("MPACT   (dense) ", sparsity, net, x)
    # runbench_eager("PyTorch (sparse)", sparsity, net, s)
    runbench_mpact("MPACT   (sparse)", sparsity, net, s)
