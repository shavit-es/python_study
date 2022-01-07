import json
from PIL import Image

file_path = ""
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)
    for ele in json_data['data']:
        try:
            imagei = Image.open(경로+ele['fileName'])
            for i in range(len(ele['regionLabel'])):
                left, up, right, down = ele['regionLabel'][i]['x'], ele['regionLabel'][i]['y'], ele['regionLabel'][i]['x']+ele['regionLabel'][i]['width'], ele['regionLabel'][i]['y']+ele['regionLabel'][i]['height']
                imageicropped = imagei.crop((left, up, right, down))
                imageicropped.save("croppedimage/"+ele["fileName"][:-4]+"_label"+str(i)+".jpg")
            print(ele['fileName']+' done')
        except FileNotFoundError as f:
            print('error : '+ ele['fileName'], f)
            continue
        except IndexError as e:
            print("not used" + ele['fileName'], e)
    print('done')
