import torch
import torch.nn.functional as F


class GraphAttentionLayer(torch.nn.Module):
    def __init__(
        self,
        in_features: int,
        out_features: int,
        n_heads: int,
        dropout: float = 0.4,
        leaky_relu_slope: float = 0.2,
    ):
        super(GraphAttentionLayer, self).__init__()
        self.n_heads = n_heads
        self.dropout = dropout
        self.n_hidden = out_features
        self.W = torch.nn.Parameter(
            torch.empty(size=(in_features, self.n_hidden * n_heads))
        )
        self.a = torch.nn.Parameter(torch.empty(size=(n_heads, 2 * self.n_hidden, 1)))
        self.leakyrelu = torch.nn.LeakyReLU(leaky_relu_slope)
        self.softmax = torch.nn.Softmax(dim=1)
        torch.nn.init.ones_(self.W)
        torch.nn.init.ones_(self.a)

    def forward(self, h: torch.Tensor, adj_mat: torch.Tensor):
        n_nodes = h.shape[0]
        h_transformed = torch.mm(h, self.W)
        h_transformed = F.dropout(h_transformed, self.dropout, training=self.training)
        h_transformed = h_transformed.view(
            n_nodes, self.n_heads, self.n_hidden
        ).permute(1, 0, 2)
        e = self._get_attention_scores(h_transformed)
        connectivity_mask = -9e16 * torch.ones_like(e)
        e = torch.where(adj_mat > 0, e, connectivity_mask)
        attention = F.softmax(e, dim=-1)
        attention = F.dropout(attention, self.dropout, training=self.training)
        h_prime = torch.matmul(attention, h_transformed)
        return h_prime.mean(dim=0)

    def _get_attention_scores(self, h_transformed: torch.Tensor):
        source_scores = torch.matmul(h_transformed, self.a[:, : self.n_hidden, :])
        target_scores = torch.matmul(h_transformed, self.a[:, self.n_hidden :, :])
        e = source_scores + target_scores.mT
        return self.leakyrelu(e)


class GAT(torch.nn.Module):
    """
    Graph Attention Network (GAT) inspired by <https://arxiv.org/pdf/1710.10903.pdf>.
    """

    def __init__(
        self,
        in_features,
        n_hidden,
        n_heads,
        num_classes,
        dropout=0.4,
        leaky_relu_slope=0.2,
    ):
        super(GAT, self).__init__()
        self.gat1 = GraphAttentionLayer(
            in_features=in_features,
            out_features=n_hidden,
            n_heads=n_heads,
            dropout=dropout,
            leaky_relu_slope=leaky_relu_slope,
        )
        self.gat2 = GraphAttentionLayer(
            in_features=n_hidden,
            out_features=num_classes,
            n_heads=1,
            dropout=dropout,
            leaky_relu_slope=leaky_relu_slope,
        )

    def forward(self, input_tensor: torch.Tensor, adj_mat: torch.Tensor):
        x = self.gat1(input_tensor, adj_mat)
        x = F.elu(x)
        x = self.gat2(x, adj_mat)
        return F.log_softmax(x, dim=1)


def gat46483():
    return GAT(in_features=4, n_hidden=64, n_heads=8, num_classes=3)
