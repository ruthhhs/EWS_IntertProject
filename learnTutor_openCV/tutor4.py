import cv2

cap = cv2.VideoCapture(0)

while True :
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # membuat garis (letak, titik awal, titik akhir, bgr, tebal garis)
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10) #blue
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 10) #green
    # membuat persegi
    img = cv2.rectangle(img, (100, 100), (200, 200), (100, 100, 100), -1) #grey solid
    img = cv2.rectangle(img, (100, 210), (200, 310), (100, 100, 100), 5) #grey border
    # membuat lingkaran (titik akhir digndti ke radius)
    img = cv2.circle(img, (320, 240), 60, (0, 0, 255), -1) #red solid

    # membuat font
    font = cv2.FONT_HERSHEY_SIMPLEX
    # text (letak, 'text', posisi tengah(x, y), font, ukuran, warna, tebal text, atribut disarankan)
    img = cv2.putText(img, 'Hello world!', (50, height - 10), font, 3, (0, 0, 0), 5)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()