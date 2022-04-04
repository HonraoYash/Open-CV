import numpy as np 
import cv2 

cap=cv2.VideoCapture(0)

while True:
    Ret,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))

    image=np.zeros(frame.shape,np.uint8)
    smallerframe=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    image[:height//2,:width//2]=smallerframe
    image[height//2:,:width//2]=smallerframe
    image[:height//2,width//2:]=smallerframe
    image[height//2:,width//2:]=smallerframe

    cv2.imshow('frame',image)

    if cv2.waitKey(1)==ord('s'):
      break

cap.release()

cv2.destroyAllWindows

