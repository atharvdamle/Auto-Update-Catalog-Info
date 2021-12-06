#!/usr/bin/env python3

from PIL import Image
import os

path = os.path.join(os.getcwd(), 'supplier-data/images')
for filename in os.listdir(path):
    if filename.endswith('.tiff'):
        print(filename)
        im = Image.open(path+'/'+filename)
        im = im.convert('RGB')
        name = filename.split('.')
        im.resize((600,400)).save(path+'/'+name[0]+'.jpg', format = "JPEG")
