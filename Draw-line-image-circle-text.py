import numpy as np 
import cv2 

cap=cv2.VideoCapture(0)

while True:
    Ret,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))

    image=cv2.line(frame,(0,0),(width,height),(255,0,0),10)
    image=cv2.line(image,(width,0),(0,height),(255,0,0),10)
    image=cv2.rectangle(image,(300,300),(500,500),(130,130,130),-1)
    image=cv2.circle(image,(400,400),100,(255,0,255),-1)

    font=cv2.FONT_ITALIC
    img=cv2.putText(image,'Yash is great!!',(10,height-10),font,2,(0,0,0),5)

    cv2.imshow('frame',image)

    if cv2.waitKey(1)==ord('s'):
      break

cap.release()

cv2.destroyAllWindows

