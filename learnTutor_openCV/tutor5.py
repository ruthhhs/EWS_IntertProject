import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True :
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # BGR --> HSV : Hue(color), Saturation(black), Value(white)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_color = np.array([100, 30, 30]) # batas gelap
    upper_color = np.array([130, 255, 255]) # batas terang
    # malah mendetek warna wajah wkwkwkwk

    # masking warna tertentu di bit tertentu (dengan metode AND)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()