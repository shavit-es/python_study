import cv2
import numpy as np
import os
path='한글이 포함된 경로'
file_list=os.listdir(path)
for imagename in file_list:
    full_path=path+imagename
    img_array=np.fromfile(full_path, np.uint8)
    img=cv2.imdecode(img_array,cv2.IMREAD_COLOR)
    resized_img = cv2.resize(img, dsize=(1024,1024),interpolation=cv2.INTER_AREA)
    cv2.imwrite('resized/'+imagename, resized_img)
    print(imagename,'done')
