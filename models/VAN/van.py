import numpy as np
from pathlib import Path
import torch
import torch.nn as nn

from models.backbone.resnet import resnet50
from models.STAR.star.pytorch.star import STAR


class VAN(nn.Module):
    def __init__(self, device) -> None:
        # Set device for model
        self.device = device

        # Define feature extractor (ResNet-50)
        self.feature_extractor = resnet50(pretrained=True)

        # Set up STAR for 3D human model
        self.num_betas = 10
        self.batch_size = 1

        self.star = STAR(gender='neutral')
        self.betas = torch.from_numpy(
            np.array(
                [
                np.array([ 2.25176191, -3.7883464, 0.46747496, 3.89178988,
                        2.20098416, 0.26102114, -3.07428093, 0.55708514,
                        -3.94442258, -2.88552087])
                ]
            )
        ).to(self.device)

        pass

    def forward(self, x):
        # Run feature extractor on input
        features = self.feature_extractor(x)

        # Run STAR for 3D human model
        poses = torch.FloatTensor(np.zeros((self.batch_size, 72))).to(self.device)
        trans = torch.FloatTensor(np.zeros((self.batch_size, 3))).to(self.device)
        model = self.star.forward(poses, self.betas, trans)
        shaped = model.v_shaped[-1, :, :]

        pass