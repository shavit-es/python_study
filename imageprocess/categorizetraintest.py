import json
from PIL import Image, ImageDraw
with open("ulcerative colitis classification.json", 'r', encoding='UTF-8') as json_file:
    json_data=json.load(json_file)
    for ele in json_data['data']:
        try:
            imagei = Image.open('C:/Users/Neurocle/Desktop/HH/code/onefolder내시경/'+ele['fileName'])
            if ele['set'] == 'test':
                imagei.save("testset/"+ele['fileName'])
            elif ele['set'] == 'train':
                imagei.save("trainset/"+ele['fileName'])
            else:
                print(ele['fileName']+' 오류')
            print(ele['fileName']+' done')
        except FileNotFoundError as f:
            print('error : '+ ele['fileName'], f)
            continue
        except IndexError as e:
            print("not used" + ele['fileName'], e)
print('done')