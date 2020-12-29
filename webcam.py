import numpy as np
import cv2
factor = 0.75

# cap = cv2.VideoCapture('dti2.asf')
# cap = cv2.VideoCapture(1)
# cap = cv2.VideoCapture('rtsp://admin:888888@192.168.1.29:10554/tcp/av0_0')
# cap = cv2.VideoCapture('rtsp://admin:admin@192.168.1.28/user=admin_password=admin_channel=1_stream=0.sdp')
# cap = cv2.VideoCapture('rtsp://192.168.1.28/profile1')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame,(0,0),fx=factor,fy=factor)
    # frame = cv2.flip(frame,0)
    # frame = cv2.flip(frame,1)
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.VideoWriter()
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
