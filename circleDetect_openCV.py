import cv2
import numpy as np

# cam = cv2.VideoCapture('assets/orangBall.mp4')
cam = cv2.VideoCapture(0)


while True :
    ret, frame = cam.read()
    if not ret :
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (15, 15), 0)
    circle = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.2, 1000, param1=100, param2=40, minRadius=50, maxRadius=300)

    if circle is not None :
        circle = np.uint16(np.around(circle))
        for i in circle[0, :] :
            cv2.circle(frame, (i[0], i[1]), 1, (0,255,0), 2) # center detect
            cv2.circle(frame, (i[0], i[1]), i[2], (255,0,255), 2) # outer detect
            cv2.putText(frame, "Lingkaran", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,255), 3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q') :
        break

cam.release()
cv2.destroyAllWindows()