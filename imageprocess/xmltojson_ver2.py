from typing import OrderedDict
import xmltodict
import json
import os
path='C:/Users/QA/Desktop/미생물/220222_수신 data/'
file_data=OrderedDict()
file_data["name"] = 30
file_data["label_type"]="box"
file_data["source"] ="labelset"
file_data["time"] = "2022-02-23T03:18:32.134Z"
file_data["version"]="2.3.3"
data=[]
file_list=os.listdir(path)
for folder in file_list:
    new_path=path+folder+"/"
    new_file_list=os.listdir(new_path)
    for ele in new_file_list:
        if ele[-4:]=='.xml':
            datasource = open(new_path+ele,'rb')
            dictionary1 = xmltodict.parse(datasource)
            appender={"fileName": ele[:-4]+'.jpg',"set": "train","classLabel": ""}
            regionLabel=[]
            # print("annotation:",dictionary1['annotation'])
            # print("len:",len(dictionary1['annotation']['object']))
            # print(ele)
            nobox = False
            try:
                bool= str(type(dictionary1['annotation']['object']))=="<class 'list'>"
                # print(bool)
            except:
                nobox=True
            if nobox: # 박스가 없는 경우
                continue
            elif bool: #박스가 한 개 이상인 경우
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
                    datasource = open(new_path+ele,'rb')
                    regionLabel.append({"className": iele['name'],"type": "Rect","x": x,"y": y,"width": width,"height": height})
            else: #박스가 여러개인경우
                x = int(dictionary1['annotation']['object']['bndbox']['xmin'])
                y= int(dictionary1['annotation']['object']['bndbox']['ymin'])
                xmax=int(dictionary1['annotation']['object']['bndbox']['xmax'])
                ymax=int(dictionary1['annotation']['object']['bndbox']['ymax'])
                width=xmax - x
                height = ymax - y
                datasource = open(new_path+ele,'rb')
                regionLabel.append({"className": dictionary1['annotation']['object']['name'],"type": "Rect","x": x,"y": y,"width": width,"height": height})
            appender["regionLabel"]=regionLabel
            data.append(appender)
            print(ele+"done")
        else: #xml 파일이 아닌 경우
            continue
     
file_data["data"]=data
f = open('label.json','w')
f.write(json.dumps(file_data, ensure_ascii=False, indent="    "))
f.close()