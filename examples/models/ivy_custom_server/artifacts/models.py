import ivy

class Regressor(ivy.Module):
    def __init__(self, input_dim, output_dim, is_training=True):
        self.linear = ivy.Linear(input_dim, output_dim)
        self.dropout = ivy.Dropout(0.5, training=is_training)
        ivy.Module.__init__(self)

    def _forward(self, x, ):
        x = ivy.sigmoid(self.linear(x))
        x = self.dropout(x)
        return x

input_dim = 3
output_dim = 1
backend = 'torch'
