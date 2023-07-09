#!/usr/bin/env python3
from PIL import Image
import os

origin_path = "./supplier-data/images/"
destiny_path = "./supplier-data/images/"

for filename in os.listdir(origin_path):
        file = os.path.join(origin_path + filename) 
        print(os.path.splitext(file)[1].lower())
        if ".tiff" == os.path.splitext(file)[1].lower():
                im = Image.open(file)
                root, _ = os.path.splitext(filename)
                renamed = destiny_path + root  + ".jpeg"
                modified = im.resize((600, 400)).convert("RGB")
                modified.save(renamed, "JPEG")
