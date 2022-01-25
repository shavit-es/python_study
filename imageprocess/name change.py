import cv2
import os
path='masks/'
file_list=os.listdir(path)
for imagename in file_list:
    img = cv2.imread('masks/'+imagename)
    cv2.imwrite('redmasks/'+imagename[:-4]+'_disease.png', img)