import numpy as np
import torch
import torch.nn as nn
import PIL.Image


class SimpleConvNet(nn.Module):
    """
    Simple Convolutional Neural Network
    """

    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(1, 10, kernel_size=3),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(26 * 26 * 10, 50),
            nn.ReLU(),
            nn.Linear(50, 20),
            nn.ReLU(),
            nn.Linear(20, 10),
        )
        print('Completed SimpleConvNet init')

    def forward(self, x):
        return self.layers(x)

    def predict(self, X, features_names):
        data = PIL.Image.open(str(X))
        data = np.array(data)
        data = torch.from_numpy(data).float()
        data = data.unsqueeze(0).unsqueeze(0)
        data = torch.nn.functional.interpolate(data, size=28, mode='bicubic', align_corners=False)
        with torch.no_grad():
            raw_output = self.layers(data)
            _, pred = torch.max(raw_output, 1)
            return pred.detach().cpu().numpy()


def main():
    c = SimpleConvNet()
    res = c.predict("samples/1.png")
    print(res)

if __name__ == "__main__":
    main()
