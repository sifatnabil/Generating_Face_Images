import os

import torch
import torchvision

from src.models.generator_model import Generator
from src.models.hyperparameters import *
from src.visualization.visualize import show

ROOT_DIR = os.path.abspath(os.curdir)
saved_model_path = os.path.join(ROOT_DIR, 'models', 'gen_model.pth')

model = Generator(NOISE_DIM, CHANNELS_IMG, FEATURES_GEN)
model.load_state_dict(torch.load(saved_model_path))
model.eval()

noise = torch.randn(BATCH_SIZE, NOISE_DIM, 1, 1)
fake = model(noise)
images = torchvision.utils.make_grid(
    fake, normalize=True
)

show(images);