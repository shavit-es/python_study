from typing import OrderedDict
import xmltodict
import json
import os
path='C:/Users/Neurocle/Desktop/HH/학습용 DB/손 골절/train/'
file_data=OrderedDict()
file_data["name"] = 30
file_data["label_type"]="box"
file_data["source"] ="labelset"
file_data["time"] = "2022-01-25T04:45:48.391Z"
file_data["version"]="2.3.3"
data=[]
file_list=os.listdir(path)
for ele in file_list:
    if ele[-4:]=='.xml':
        datasource = open(path+ele,'rb')
        dictionary1 = xmltodict.parse(datasource)
        appender={"fileName": ele[:-4]+'.jpg',"set": "train","classLabel": ""}
        regionLabel=[]
        # print(dictionary1['annotation'])
        # print(len(dictionary1['annotation']['object']))
        if len(dictionary1['annotation']['object'])<5: #골절이 한 개 이상인 경우
            for iele in dictionary1['annotation']['object']:
                x = int(iele['bndbox']['xmin'])
                y= iele['bndbox']['ymin']
                y=int(y)
                xmax=iele['bndbox']['xmax']
                xmax=int(xmax)
                width = xmax - x
                ymax=iele['bndbox']['ymax']
                ymax=int(ymax)
                height=ymax-y
                datasource = open(path+ele,'rb')
                regionLabel.append({"className": "Fraction","type": "Rect","x": x,"y": y,"width": width,"height": height})
        else:
            x = int(dictionary1['annotation']['object']['bndbox']['xmin'])
            y= int(dictionary1['annotation']['object']['bndbox']['ymin'])
            xmax=int(dictionary1['annotation']['object']['bndbox']['xmax'])
            ymax=int(dictionary1['annotation']['object']['bndbox']['ymax'])
            width=xmax - x
            height = ymax - y
            datasource = open(path+ele,'rb')
            regionLabel.append({"className": "Fraction","type": "Rect","x": x,"y": y,"width": width,"height": height})
        appender["regionLabel"]=regionLabel
        data.append(appender)
        print(ele+"done")
    else:
        continue
     
file_data["data"]=data
f = open('label.json','w')
f.write(json.dumps(file_data, ensure_ascii=False, indent="\t"))
f.close()