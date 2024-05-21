# RUN: %PYTHON %s | FileCheck %s

import torch

from mpactbackend import mpact_jit, mpact_jit_compile, mpact_jit_run


def spike(input):
    return (input >= 0).float()


def sqSum(input):
    return (input * input).sum()


class LIF(torch.nn.Module):
    def __init__(self):
        super(LIF, self).__init__()
        self.thresh = 1.0
        self.decay = 0.5
        self.act = spike

    def forward(self, X):
        """A filter that yields a binary-valued sparse tensor."""
        mem = 0
        spike_pot = []
        T = X.size(-1)
        for t in range(T):
            mem = mem * self.decay + X[..., t]
            spike = self.act(mem - self.thresh)
            spike = spike.to_sparse().to_dense()  # prop hack
            mem = mem * (1.0 - spike)
            spike_pot.append(spike)
        spike_pot = torch.stack(spike_pot, dim=-1)
        return spike_pot


class tdLayer(torch.nn.Module):
    def __init__(self, layer):
        super(tdLayer, self).__init__()
        self.layer = layer

    def forward(self, X):
        T = X.size(-1)
        out = []
        for t in range(T):
            m = self.layer(X[..., t])
            out.append(m)
        out = torch.stack(out, dim=-1)
        return out


class Block(torch.nn.Module):
    def __init__(self):
        super(Block, self).__init__()
        self.spike = LIF()
        self.layer = tdLayer(sqSum)

    def forward(self, X):
        out = self.spike(X)
        out = self.layer(out)
        return out


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
