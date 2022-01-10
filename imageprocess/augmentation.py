import os
from PIL import Image
path=''
file_list=os.listdir(path)
#이미지 불러오기
for filename in file_list[:-1]:
    image1 = Image.open(path+'/'+filename)
    FlipImage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    FlipImage1.save(''+filename[:-4]+'_transposedlr.png')
    FlipImage2 = image1.transpose(Image.FLIP_TOP_BOTTOM)
    FlipImage2.save(''+filename[:-4]+'_transposedtb.png')
    RotateImage1=image1.transpose(Image.ROTATE_90)
    RotateImage1.save(''+filename[:-4]+'_transpose90.png')
    RotateImage2=RotateImage1.transpose(Image.ROTATE_90)
    RotateImage2.save(''+filename[:-4]+'_transpose180.png')
    RotateImage3=RotateImage2.transpose(Image.ROTATE_90)
    RotateImage3.save(''+filename[:-4]+'_transpos270.png')
