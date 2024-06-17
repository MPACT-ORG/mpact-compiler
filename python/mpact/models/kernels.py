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


class FeatureScale(torch.nn.Module):
    def forward(self, F):
        sum_vector = torch.sum(F, dim=1)
        reciprocal_vector = 1 / sum_vector
        reciprocal_vector[reciprocal_vector == float("inf")] = 0
        scaling_diagonal = torch.diag(reciprocal_vector).to_sparse()
        return scaling_diagonal @ F


class Normalization(torch.nn.Module):
    def forward(self, A):
        sum_vector = torch.sum(A, dim=1)
        reciprocal_vector = 1 / sum_vector
        reciprocal_vector[reciprocal_vector == float("inf")] = 0
        scaling_diagonal = torch.diag(reciprocal_vector).to_sparse()
        return scaling_diagonal @ A @ scaling_diagonal
