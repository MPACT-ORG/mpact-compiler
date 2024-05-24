import torch

class GraphConv(torch.nn.Module):
    def __init__(self, input_dim, output_dim):
        super(GraphConv, self).__init__()
        self.kernel = torch.nn.Parameter(torch.Tensor(input_dim, output_dim))
        torch.nn.init.ones_(self.kernel)
        self.bias = torch.nn.Parameter(torch.Tensor(output_dim))
        torch.nn.init.ones_(self.bias)

    def forward(self, inp, adj_mat):
        # Input matrix times weight matrix.
        support = torch.mm(inp, self.kernel)
        # Sparse adjacency matrix times support matrix.
        output = torch.spmm(adj_mat, support)
        # Add bias.
        output = output + self.bias
        return output
