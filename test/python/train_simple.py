# RUN: %PYTHON %s | FileCheck %s

import torch
import numpy as np

from torch.utils.data import Dataset, DataLoader

from mpact.mpactbackend import mpact_jit
from mpact.models.kernels import SimpleNet
from mpact.models.train import training_loop


A = torch.tensor(
    [
        [
            [1.0, 1.0, 1.0, 1.0],
            [0.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
        ],
        [
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0, 0.0],
        ],
        [
            [1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 0.0],
        ],
        [
            [0.0, 0.0, 0.0, 1.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
        ],
    ],
    dtype=torch.float32,
)


B = torch.tensor(
    [
        [
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
        ],
        [
            [1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0],
        ],
    ],
    dtype=torch.float32,
)

# Labels 0:sparse 1:dense

labA = torch.tensor([1, 0, 1, 0])

labB = torch.tensor([0, 1])

# A toy training and validation data set consisting of dense/sparse tensors.


class TrainData(Dataset):
    def __len__(self):
        return A.shape[0]

    def __getitem__(self, index):
        return A[index], labA[index]


class ValidationData(Dataset):
    def __len__(self):
        return B.shape[0]

    def __getitem__(self, index):
        return B[index], labB[index]


train_data = TrainData()
validation_data = ValidationData()

net = SimpleNet()
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)
loss_function = torch.nn.CrossEntropyLoss()
train = DataLoader(train_data, batch_size=2)
validation = DataLoader(validation_data, batch_size=2)


# Run it with PyTorch.
# CHECK-LABEL: pytorch
# CHECK:       Epoch 99
# CHECK-SAME:  Accuracy = 1.00
print("pytorch")
training_loop(net, optimizer, loss_function, train, validation, epochs=100)

# Run it with MPACT.
# CHECK-LABEL: mpact
print("mpact")
# TODO: teach MPACT about autograd
