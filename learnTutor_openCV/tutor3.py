import cv2
import numpy as np

# 0 menunjukkan jumlah webcam = 1 --> 0 itu bawaan perangkat
cap = cv2.VideoCapture(0)
# kalau mau pake video dalem kurungnya ('link video')

while True :
    # read memanggil frame (video kita)
    # ret menunjukkan apakah fungsi berjalan dengan baik atau tidak --> boolean
    ret, frame = cap.read()
    # mengetahui ukuran panjang dan tinggi frame
    width = int(cap.get(3))
    height = int(cap.get(4))

    # membuat box kosong dengan ukuran frame asli
    image = np.zeros(frame.shape, np.uint8)
    # mengubah ukuran frame agar muat di box
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    
    # membuat frame kecil 4x + rotate
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180) # top l
    image[height//2:, :width//2] = smaller_frame # bottom l
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) # top r
    image[height//2:, width//2:] = smaller_frame # bottom r

    cv2.imshow('frame', image)

    # mengeluarkan frame dengan menekan q
    if cv2.waitKey(1) == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()