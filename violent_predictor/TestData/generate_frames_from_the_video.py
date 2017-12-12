import cv2
import sys

vid_name = sys.argv[1]
import os
vidcap = cv2.VideoCapture(vid_name)
success,image = vidcap.read()
count = 0
success = True
os.chdir("C:\\Users\\Stark\\Desktop\\Programming\\Projects\\CleverNator\\Past\\Rest\\TestData\\test")
# os.chdir(path)
while success:
  success, image = vidcap.read()
  if count % 100 == 0:
    print('Read a new frame: ', count)
    cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1
