import json
from PIL import Image
import os

file_path = "./part.json"
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)
    for ele in json_data['data']:
        try:
            imagei = Image.open('파일경로')
            left, up, right, down = ele['regionLabel'][0]['x'], ele['regionLabel'][0]['y'], ele['regionLabel'][0]['x']+ele['regionLabel'][0]['width'], ele['regionLabel'][0]['y']+ele['regionLabel'][0]['height']
            imagei = imagei.crop((left, up, right, down))
            imagei.save("파일경로")
        except:
            continue
        print(ele['fileName']+' done')
