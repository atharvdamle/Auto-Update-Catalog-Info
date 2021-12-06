#! /usr/bin/env python3

import os
import requests

path = os.path.join(os.getcwd(), 'supplier-data/descriptions')
for filename in os.listdir(path):
    with open(path + '/' + filename, 'r') as f:
        name = filename.split('.')
        text = f.readlines()
        text = [line[:-1] for line in text]
        data = {'name': text[0], 'weight': int(text[1].replace(' lbs', '')), 'description': text[2], 'image_name': name[0]+'.jpeg'}
        print(data)
        url = 'http://localhost/fruits/'
        r = requests.post(url, data = data)
        print(r.status_code)
