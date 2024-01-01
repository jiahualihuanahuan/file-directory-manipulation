import os
import shutil
from tqdm import tqdm

base_path = "C:/folder"

images = [f for f in os.listdir(base_path) if '.jpg' in f.lower()]

for image in tqdm(images):
    subfolder_name = image[:1]
    old_path = f"{base_path}/{image}"
    new_path = f"{base_path}/{subfolder_name}"
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    try:
        shutil.move(old_path, new_path)
    except:
        pass
