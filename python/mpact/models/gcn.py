import torch
import torch.nn.functional as F


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


class GCN(torch.nn.Module):
    """
    Graph Convolutional Network (GCN) inspired by <https://arxiv.org/pdf/1609.02907.pdf>.
    """

    def __init__(self, input_dim, hidden_dim, output_dim, dropout_p=0.1):
        super(GCN, self).__init__()
        self.gc1 = GraphConv(input_dim, hidden_dim)
        self.gc2 = GraphConv(hidden_dim, output_dim)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, input_tensor, adj_mat):
        x = self.gc1(input_tensor, adj_mat)
        x = F.relu(x)
        x = self.dropout(x)
        x = self.gc2(x, adj_mat)
        return F.log_softmax(x, dim=1)


def graphconv4_4():
    return GraphConv(input_dim=4, output_dim=4)


def gcn4_16_4():
    return GCN(input_dim=4, hidden_dim=16, output_dim=4)
