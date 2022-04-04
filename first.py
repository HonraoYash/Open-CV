import cv2

img=cv2.imread('images/car.png',-1)
img=cv2.resize(img,(1000,1000))
img=cv2.rotate(img,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('images/newimg.jpg',img)


cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()