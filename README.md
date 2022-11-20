# Generate Cartoonish Faces Using DCGAN

## Introduction

Image generation is the task of generating new images from an existing dataset. It has been an active area of research for a long time. Generating images that are not in the original data is both an interesting and complex problem. GANs are very popular in the task of image generation. My goal in this project was to generate synthetic face images
using [DCGAN](https://arxiv.org/pdf/1511.06434v2.pdf). 3D face models
can be used in different tasks like game character model designing, animation character designing, and creating each character can take time and effort. Generating character faces using a model would help in such cases, reducing the time needed to generate new, previously unseen faces.

## Dataset

The Dataset [Synthetic Faces High Quality (SFHQ) part 2](https://www.kaggle.com/datasets/selfishgene/synthetic-faces-high-quality-sfhq-part-2?resource=download) was collected from Kaggle which contained 90K curated 1024 X 1024 size face images. For my work, I used 60K images and initially resized them to 256 x 256. This dataset contains a high degree of variability on the axes of identity, ethnicity, age, pose, expression, lighting conditions, hair style, hair-color, and facial hair.

## Project Installation

First, Install PyTorch either the GPU or the CPU version according to GPU availablity from [here](https://pytorch.org/). Then run:

```python
pip install -r requirements.txt
```

## Project Sturcture

```text
|-data
|   |-> processed <- for processed data
|   |-> raw <- for raw data
|-models <- stores the saved models
|-notebooks <- necessary and experimental notebooks
|-reports 
|-src
|   |-> data
|       |- make_dataset.py <- data processing
|   |-> models
|       |- discriminator_model.py 
|       |- generator_model.py
|       |- hyperparameters.py
|       |- inference_model.py <- inference using saved model
|       |- train_model.py
|   |-> visualization
|       |->visualize.py <- visualize results of inference
|-.env
|-requirements.txt
```

To run the project after everything is set up and dataset is in place, run:

```python
python -m src.models.train_model or # to train the model
python -m src.models.inference_model # For inference
```

**To see a Summary of the training process and metrics you can visit here: [WandB Run](https://wandb.ai/sifatnabil/pytorch-project-test/runs/2n91n68u/overview)**

