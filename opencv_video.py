import cv2

capture=cv2.VideoCapture("Resources/dog.mp4")

while True:
    success,img=capture.read()

    cv2.imshow("img",img)

    if cv2.waitKey(20)&0xff==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()