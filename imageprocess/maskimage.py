import json
from PIL import Image, ImageDraw

file_path = "./part.json"
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)
    for ele in json_data['data']:
        try:
            imagei = Image.open('C:/Users/QA/Desktop/HH/prestudy/swissgoldbar/image/'+ele['fileName'])
            left, up, right, down = ele['regionLabel'][0]['x'], ele['regionLabel'][0]['y'], ele['regionLabel'][0]['x']+ele['regionLabel'][0]['width'], ele['regionLabel'][0]['y']+ele['regionLabel'][0]['height']
            cropped = imagei.crop((left, up, right, down))
            mask=Image.new("RGB",imagei.size, color="#000")
            mask.paste(cropped,(left,up))
            mask.save("C:/Users/QA/Desktop/HH/prestudy/swissgoldbar/maskedimages/"+ele['fileName'])
            print(ele['fileName']+' done')
        except:
            print('missing file : '+ ele['fileName'])
            continue
print('done')
