import numpy as np
import cv2
import sys
import time
from Camera import camera
factor = 0.4
# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('rtsp://admin:88888888@{}:10554/tcp/av0_0'.format('172.30.71.131'))
# cap = cv2.VideoCapture('http://admin:admin@192.168.0.102/videostream.asf?usr=admin&pwd=admin')
# cap = cv2.VideoCapture('rtsp://admin:qwer1234@172.30.71.119:554/Streaming/channels/1')
cap = camera('rtsp://admin:qwer1234@192.168.1.76:554/Streaming/channels/1')
n = 0 
current = time.time()
while(True):
    # Capture frame-by-frame
    # ret, frame = cap.read()
    frame = cap.get_frame()
    ret = True
    # print(frame.shape)
    # frame = cv2.resize(frame,(0,0),fx=factor,fy=factor)
    # Display the resulting frame
    # cv2.imshow('frame',frame)
    # frame = cv2.flip(frame,0)
    if ret==True:
        cv2.imshow('dome camera',frame)
        # img_str = cv2.imencode('.jpg', frame)[1].tostring()
        # sys.stdout.write(cv2.imdecode('.png',frame)[1].tostring())
        # sys.stdout.write(str(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    now = time.time()
    if now > current+1:
        current = now
        print("FPS : {}".format(n))
        n = 0
    n+=1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()