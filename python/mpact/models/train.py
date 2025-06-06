import torch
import torch.nn.functional as F


def num_all_parameters(model):
    """Returns the number of all parameters in a model."""
    return sum(p.numel() for p in model.parameters())


def num_parameters(model):
    """Returns the number of trainable parameters in a model."""
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


def training_loop(model, optimizer, loss_function, train, validation, epochs=10):
    """A rudimentary PyTorch training loop for classification with training and validation data."""
    for epoch in range(epochs):
        # Switch to training mode.
        model.train()
        tloss = 0.0
        num_train = len(train)  # in batches
        for inp, target in train:  # batch loop (training)
            optimizer.zero_grad()
            output = model(inp)
            loss = loss_function(output, target)
            loss.backward()
            optimizer.step()
            tloss += loss.data.item()

        # Switch to inference mode.
        model.eval()  # disables e.g. model drop-out
        with torch.no_grad():  # disables gradient computations
            vloss = 0.0
            num_validation = len(validation)  # in batches
            num_correct = 0
            num_total = 0
            for inp, target in validation:  # batch loop (validation)
                output = model(inp)
                loss = loss_function(output, target)
                vloss += loss.data.item()
                correct = torch.eq(
                    torch.max(F.softmax(output, dim=1), dim=1)[1], target
                ).view(-1)
                num_correct += torch.sum(correct).item()
                num_total += correct.shape[0]

        # Report stats.
        print(
            "Epoch {:d}, Training loss = {:.2f} #{:d}, Validation loss = {:.2f} #{:d}, Accuracy = {:.2f} #{:d}".format(
                epoch,
                (tloss / num_train) if num_train != 0 else 0,
                num_train,
                (vloss / num_validation) if num_validation != 0 else 0,
                num_validation,
                (num_correct / num_total) if num_total != 0 else 0,
                num_total,
            )
        )
