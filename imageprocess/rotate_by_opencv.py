import cv2
import os

def createRotate(centerpoint, angle, src):
    rot = cv2.getRotationMatrix2D(centerpoint, angle, 1) # 20도 회전, 스케일 그대로
    dst = cv2.warpAffine(src, rot, (0, 0))
    cv2.imwrite('rotated/'+imagename[:-4]+'_rot'+str(angle)+'.jpg', dst)
def createFlip(src, updown):
    dst=cv2.flip(src,updown)
    cv2.imwrite('rotated/'+imagename[:-4]+'_flip'+str(updown)+'.jpg', dst)
path = '폴더경로/'
file_list=os.listdir(path)
for imagename in file_list:
    src = cv2.imread(path+imagename)
    cp = (src.shape[1]/2, src.shape[0]/2) #중심점
    for i in range(30,360,30):
        createRotate(cp,i,src)
    createFlip(src, 1)
    createFlip(src, 0)
    print(imagename,'done')
