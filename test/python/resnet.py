# RUN: %PYTHON %s | FileCheck %s

import torch
import numpy as np

from mpact.mpactbackend import mpact_jit, mpact_jit_compile, mpact_jit_run


def spike(input):
    return (input >= 0).float()


class Straight(torch.nn.Module):
    def forward(self, input):
        return input


class tdLayer(torch.nn.Module):
    def __init__(self, layer, bn=None):
        super(tdLayer, self).__init__()
        self.layer = layer
        self.bn = bn if bn is not None else Straight()

    def forward(self, X):
        T = X.size(-1)
        out = []
        for t in range(T):
            m = self.layer(X[..., t])
            out.append(m)
        out = torch.stack(out, dim=-1)
        out = self.bn(out)
        return out


class LIF(torch.nn.Module):
    def __init__(self):
        super(LIF, self).__init__()
        self.thresh = 1.0
        self.decay = 0.5
        self.act = spike
        self.gama = 1.0

    def forward(self, X, gama=1):
        mem = 0
        spike_pot = []
        T = X.size(-1)
        for t in range(T):
            mem = mem * self.decay + X[..., t]
            spike = self.act(mem - self.thresh)
            mem = mem * (1.0 - spike)
            spike_pot.append(spike)
        spike_pot = torch.stack(spike_pot, dim=-1)
        return spike_pot


class tdBatchNorm(torch.nn.BatchNorm2d):
    def __init__(
        self,
        num_features,
        eps=1e-05,
        momentum=0.1,
        alpha=1,
        affine=True,
        track_running_stats=True,
    ):
        super(tdBatchNorm, self).__init__(
            num_features, eps, momentum, affine, track_running_stats
        )
        self.alpha = alpha

    def forward(self, input):
        exponential_average_factor = 0.0
        mean = self.running_mean
        var = self.running_var
        input = (
            self.alpha
            * (input - mean[None, :, None, None, None])
            / (torch.sqrt(var[None, :, None, None, None] + self.eps))
        )
        if self.affine:
            input = (
                input * self.weight[None, :, None, None, None]
                + self.bias[None, :, None, None, None]
            )
        return input


def conv3x3(in_planes, out_planes, stride=1, groups=1, dilation=1):
    return torch.nn.Conv2d(
        in_planes,
        out_planes,
        kernel_size=3,
        stride=stride,
        padding=dilation,
        groups=groups,
        bias=False,
        dilation=dilation,
    )


def conv1x1(in_planes, out_planes, stride=1):
    return torch.nn.Conv2d(
        in_planes, out_planes, kernel_size=1, stride=stride, bias=False
    )


class BasicBlock(torch.nn.Module):
    expansion = 1

    def __init__(
        self,
        inplanes,
        planes,
        stride=1,
        downsample=None,
        groups=1,
        base_width=64,
        dilation=1,
        norm_layer=None,
    ):
        super(BasicBlock, self).__init__()
        if norm_layer is None:
            norm_layer = tdBatchNorm
            # norm_layer = nn.BatchNorm2d
        if groups != 1 or base_width != 64:
            raise ValueError("BasicBlock only supports groups=1 and base_width=64")
        if dilation > 1:
            raise NotImplementedError("Dilation > 1 not supported in BasicBlock")
        # Both self.conv1 and self.downsample layers downsample the input when stride != 1
        self.conv1 = conv3x3(inplanes, planes, stride)
        self.bn1 = norm_layer(planes)
        self.conv2 = conv3x3(planes, planes)
        self.bn2 = norm_layer(planes)
        self.downsample = downsample
        self.stride = stride
        self.conv1_s = tdLayer(self.conv1, self.bn1)
        self.conv2_s = tdLayer(self.conv2, self.bn2)
        self.spike1 = LIF()
        self.spike2 = LIF()

    def forward(self, x):
        identity = x

        out = self.conv1_s(x)
        out = self.spike1(out)
        out = self.conv2_s(out)

        if self.downsample is not None:
            identity = self.downsample(x)

        out += identity
        out = self.spike2(out)

        return out


class ResNety(torch.nn.Module):
    def __init__(
        self,
        block,
        layers,
        num_classes=10,
        zero_init_residual=False,
        groups=1,
        width_per_group=64,
        replace_stride_with_dilation=None,
        norm_layer=None,
    ):
        super(ResNety, self).__init__()
        if norm_layer is None:
            norm_layer = tdBatchNorm
            # norm_layer = nn.BatchNorm2d
        self._norm_layer = norm_layer
        self.inplanes = 64
        self.dilation = 1
        self.groups = groups
        self.base_width = width_per_group
        self.pre = torch.nn.Sequential(
            tdLayer(
                layer=torch.nn.Conv2d(
                    3, self.inplanes, kernel_size=(3, 3), stride=(1, 1)
                ),
                bn=self._norm_layer(self.inplanes),
            ),
            LIF(),
        )
        self.layer1 = self._make_layer(block, 64, layers[0], stride=2)
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2)
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2)
        self.avgpool = tdLayer(torch.nn.AdaptiveAvgPool2d((1, 1)))
        self.fc = tdLayer(torch.nn.Linear(256, num_classes))
        self.T = 6
        for m in self.modules():
            if isinstance(m, torch.nn.Conv2d):
                torch.nn.init.kaiming_normal_(
                    m.weight, mode="fan_out", nonlinearity="relu"
                )

    def _make_layer(self, block, planes, blocks, stride=1, dilate=False):
        norm_layer = self._norm_layer
        downsample = None
        previous_dilation = self.dilation
        if dilate:
            self.dilation *= stride
            stride = 1
        if stride != 1 or self.inplanes != planes * block.expansion:
            downsample = tdLayer(
                conv1x1(self.inplanes, planes * block.expansion, stride),
                norm_layer(planes * block.expansion),
            )

        layers = []
        layers.append(
            block(
                self.inplanes,
                planes,
                stride,
                downsample,
                self.groups,
                self.base_width,
                previous_dilation,
                norm_layer,
            )
        )
        self.inplanes = planes * block.expansion
        for _ in range(1, blocks):
            layers.append(
                block(
                    self.inplanes,
                    planes,
                    groups=self.groups,
                    base_width=self.base_width,
                    dilation=self.dilation,
                    norm_layer=norm_layer,
                )
            )

        return torch.nn.Sequential(*layers)

    def _forward_impl(self, input):
        out = []
        input = input.unsqueeze(-1).repeat(1, 1, 1, 1, self.T)
        x = self.pre(input)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.avgpool(x)
        x = x.view(x.size(0), -1, x.size(-1))
        x = self.fc(x)
        for t in range(self.T):
            out.append(x[..., t])
        return torch.stack(out, dim=1)

    def forward(self, x):
        return self._forward_impl(x)


resnet = ResNety(block=BasicBlock, layers=[2, 2, 2], num_classes=10)
resnet.train(False)  # switch to inference

# Get a random input.
#   B x RGB x H x W
x = torch.rand(1, 3, 16, 16)

#
# CHECK: pytorch
# CHECK: mpact
# CHECK: passed
#

with torch.no_grad():

    # Run it with PyTorch.
    print("pytorch")
    res1 = resnet(x)
    print(res1)

    # Run it with MPACT.
    # TODO: make this work
    print("mpact")
    res2 = mpact_jit(resnet, x)
    print(res2)

# Completely different inputs and weights for each run,
# so we simply verify the two results are the same.
np.testing.assert_allclose(res1.numpy(), res2, rtol=1e-5, atol=0)
print("passed")
