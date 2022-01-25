import cv2
import os
path='masks/'
file_list=os.listdir(path)
for imagename in file_list:
    img = cv2.imread('masks/'+imagename)
    print(img.shape)
    height, width = img.shape[0], img.shape[1]
    for rows in range(height):
        for columns in range(width):
            if img.item(rows, columns,2) == 128:
                img.itemset(rows,columns,0,255)
                img.itemset(rows,columns,1,255)
                img.itemset(rows,columns,2,255)
    cv2.imwrite('whitemasks/'+imagename[:-4]+'_disease.png', img)