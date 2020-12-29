import cv2
import numpy as np
from scipy import stats
import math
factor = 0.3
thres = 10
cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
frame1 = cv2.resize(frame1,(0,0),fx=factor,fy=factor)
ret = cap.set(3,320)
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
direction = 0 # l=-1 r=+1

# import paho.mqtt.client
# import paho.mqtt.publish

def gesture(massage):
	# paho.mqtt.publish.single(
	# 	topic='gesture',
	# 	payload=massage,
	# 	hostname='localhost',
	# 	port=1884,
	# )
    print(massage)

while(1):
    ret, frame2 = cap.read()
    frame2 = cv2.resize(frame2,(0,0),fx=factor,fy=factor)
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(
        prev=prvs, 
        next=next,
        flow=None, 
        pyr_scale=0.5, 
        levels=5, 
        winsize=10, 
        iterations=3, 
        poly_n=5, 
        poly_sigma=1.1, 
        flags=0)
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    Vx = flow[...,0]
    avg_Vx = np.average(Vx[np.abs(Vx)>10])
    if(math.isnan(avg_Vx)):
        if(direction<-2 or 2<direction):
            if(direction<0):
                print("LEFT")
                gesture("L")
            else:
                print("RIGHT")
                gesture("R")
        direction=0
    else:
        if(avg_Vx>0):
            direction-=1
        elif(avg_Vx<0):
            direction+=1
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    bgr = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    cv2.imshow('frame2',bgr)
    cv2.imshow('Vx',Vx)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.png',frame2)
        cv2.imwrite('opticalhsv.png',bgr)
    prvs = next
cap.release()
cv2.destroyAllWindows()
