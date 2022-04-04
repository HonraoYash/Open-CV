import cv2

img=cv2.imread('images/car.png',-1)

print(img.shape)

for i in range(200):
    for j in range(img.shape[1]):
        img[i][j]=[0,0,0]

copy=img[100:400 , 500:800]  
img[300:600 , 100:400]=copy    

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()