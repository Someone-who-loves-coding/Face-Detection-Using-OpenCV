import cv2

a = cv2.VideoCapture(0)

while True :
    ret, c= a.read()
    cv2.imshow("Live Vid", c)
    if cv2.waitKey(10) == ord("a") :
        break
c.release()