import json
from PIL import Image, ImageDraw
with open("Serial Detection.json", 'r', encoding='UTF-8') as json_file:
    json_data=json.load(json_file)
    for ele in json_data['data']:
        try:
            imagei = Image.open(direction+'ele['fileName'])
            left, up, right, down = ele['regionLabel'][0]['x'], ele['regionLabel'][0]['y'], ele['regionLabel'][0]['x']+ele['regionLabel'][0]['width'], ele['regionLabel'][0]['y']+ele['regionLabel'][0]['height']
            cropped = imagei.crop((left, up, right, down))
            mask=Image.new("RGB",imagei.size, color="#000")
            mask.paste(cropped,(left,up))
            mask.save(direction+ele['fileName'])
            print(ele['fileName']+' done')
        except FileNotFoundError as f:
            print('missing file : '+ ele['fileName'], f)
            continue
        except IndexError as e:
            print("not used" + ele['fileName'], e)
print('done')
