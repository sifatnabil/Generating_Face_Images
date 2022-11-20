import os

from PIL import Image

DATAFOLDER_PATH = 'data/raw/images'
ROOT_DIR = os.path.abspath(os.curdir)

files = os.listdir(os.path.join(ROOT_DIR, DATAFOLDER_PATH))

for file in files[:60000]:
    original_file = os.path.join(ROOT_DIR, DATAFOLDER_PATH, file)
    resized_file = os.path.join(ROOT_DIR, 'data', 'processed', file)
    
    image = Image.open(original_file)

    resized_image = image.resize((256, 256))
    resized_image.save(resized_file)
    