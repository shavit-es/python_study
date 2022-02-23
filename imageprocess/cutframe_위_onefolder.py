import cv2
import os

videoPath = 'C:/Users/QA/Desktop/HH/평가용 제공data/위/'
imagePath = 'images/'
file_list = os.listdir(videoPath)

for file in file_list:
    try:
        if not (os.path.isdir(videoPath)):
            os.makedirs(os.path.join(imagePath))
        cap = cv2.VideoCapture(videoPath + file)
        fps = cap.get(cv2.CAP_PROP_FPS)
        count = 0
        while True:
            ret, image = cap.read()
            if not ret:
                break
            if count%fps==0:
                minutes=int((count//fps)//60)
                seconds=int((count//fps)%60)
                cv2.imwrite(imagePath+file[:-4]+"_{}m{}s.jpg".format(minutes, seconds), image)
                print(file[:-4]+'_{}m{}s.jpg'.format(minutes, seconds))
            count += 1
        cap.release()
    except OSError as e:
        if e.errno != e.EEXIST:
            print("Failed to create directory!!!!!")
            raise