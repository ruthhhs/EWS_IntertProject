import cv2
import numpy as np

# cam = cv2.VideoCapture('assets/orangBall.mp4')
cam = cv2.VideoCapture(0)

while True :
    ret, frame = cam.read()
    if not ret :
        break

    blur = cv2.GaussianBlur(frame, (15, 15), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 165, 115), (10, 200, 255))
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1.2, 1000, param1=100, param2=40, minRadius=50, maxRadius=300)

    if circles is not None :
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :] :
            x, y , radius = circle
            cv2.circle(frame, (x, y), radius, (0, 0, 255), 2) # center detect
            cv2.circle(frame, (x, y), 5, (0,0,255), 2) # outer detect
            cv2.putText(frame, "Bola Oranye", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255), 3)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q') :
        break

cam.release()
cv2.destroyAllWindows()