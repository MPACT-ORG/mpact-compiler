import torch


class MVNet(torch.nn.Module):
    def forward(self, x, v):
        return torch.mv(x, v)


class MMNet(torch.nn.Module):
    def forward(self, x, y):
        return torch.mm(x, y)


class AddNet(torch.nn.Module):
    def forward(self, x, y):
        return torch.add(x, y)


class MulNet(torch.nn.Module):
    def forward(self, x, y):
        return torch.mul(x, y)


class SelfNet(torch.nn.Module):
    def forward(self, x):
        return x


class SDDMMNet(torch.nn.Module):
    def forward(self, x, y, z):
        return torch.mul(x, torch.mm(y, z))


class SqSum(torch.nn.Module):
    def forward(self, x):
        return (x * x).sum()


class CountEq(torch.nn.Module):
    def forward(self, x, s):
        nums = (x == s).sum()
        return nums


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


class SimpleNet(torch.nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        # Model parameters (weights and biases of linear layers).
        self.fc1 = torch.nn.Linear(16, 8)
        self.fc2 = torch.nn.Linear(8, 4)
        self.fc3 = torch.nn.Linear(4, 2)

    def forward(self, x):
        x = x.view(-1, 16)
        x = torch.nn.functional.relu(self.fc1(x))
        x = torch.nn.functional.relu(self.fc2(x))
        return self.fc3(x)  # assumes: softmax in loss function
