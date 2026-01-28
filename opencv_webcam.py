import cv2

capture=cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:

    _,img=capture.read()

    imgCanny=cv2.Canny(img,100,100)

    cv2.imshow("webcam",img)
    cv2.imshow("imgCanny",imgCanny)

    if cv2.waitKey(20)&0xff==ord('p'):
        break

capture.release()
cv2.destroyAllWindows()