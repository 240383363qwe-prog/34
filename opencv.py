import cv2

print(cv2.__version__)

img=cv2.imread('Resources/Jaychou.jpg')

print(img.shape)

img=cv2.resize(img,(int(img.shape[1]/1.5),int(img.shape[0]/1.5)))

cv2.imshow("Frame,",img)

cv2.waitKey(0)