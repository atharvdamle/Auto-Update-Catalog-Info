#!/usr/bin/env python3

import requests
import os

path = os.path.join(os.getcwd(), 'supplier-data/images')
for filename in os.listdir(path):
    if filename.endswith('.jpeg'):
        url = 'http://localhost/upload/'
        with open(path+'/'+filename, 'rb') as file:
            r = requests.post(url, files = {'file': file})
