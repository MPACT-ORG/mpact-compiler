import torch


class MVNet(torch.nn.Module):
    def forward(self, x, v):
        return torch.mv(x, v)


class MMNet(torch.nn.Module):
    def forward(self, x, v):
        return torch.mm(x, v)


class AddNet(torch.nn.Module):
    def forward(self, x, v):
        return torch.add(x, v)


class MulNet(torch.nn.Module):
    def forward(self, x, v):
        return torch.mul(x, v)


class SelfNet(torch.nn.Module):
    def forward(self, x):
        return x


class SDDMMNet(torch.nn.Module):
    def forward(self, x, y, z):
        return torch.mul(x, torch.mm(y, z))
