import os
import shutil
from tqdm import tqdm

base_path = "C:/"

images = [f for f in os.listdir(base_path) if '.jpg' in f.lower()]

for image in tqdm(images):
    os.remove(f"{base_path}/{image}")
