import cv2

# mendeteksi lokasi gambar
# parameter 0 --> bmw, 1 --> colour
img = cv2.imread('assets/gambar_test.jpg', 1)
# ngubah ukuran gambar
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# membuat file baru setingkat dgn file py
# cv2.imwrite('new_img.png', img)

# menampilkan gambar
cv2.imshow('yipey', img)
# parameter 0 --> wait unlimited sampai kita tekan layar
#kalau angka > 0 akan nunggu waktu dalam sekon sampai fungsi berikutnya jalan
cv2.waitKey(0)
# nutup layar pop up gambar
cv2.destroyAllWindows()

 