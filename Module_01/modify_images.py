#!/usr/bin/python3
from PIL import Image
import os

origin_path = "/home/student-03-8332e796829b/images/"
destiny_path = "/opt/icons/"

for filename in os.listdir(origin_path):
    file = os.path.join(origin_path, filename)
    #print(file)
    img = Image.open(file)
    destiny = destiny_path + filename + ".jpg"
    im = img.convert("RGB")
    resized_image =  im.rotate(90).resize((128, 128))
    resized_image.save(destiny,"JPEG")
