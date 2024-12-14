import cv2
import random

img = cv2.imread('assets/gambar_test.jpg', 1)

#    memprint pixel ke dalam bentuk matrix
print(img)
#    tipe : numpy.ndarray
print(type(img))
#    mencetak tinggi, panjang, channel(colour, misal bgr = 3 )
#    bgr --> [[0-255, 0-255, 0-255]]
print(img.shape)

#    melihat bgr [di baris ke-] dan [pixel dari- : ke-]
print(img[100][50:100])
#    bisa hanya baris ke- aja
print(img[100])
#    melihat 1 pixel aja
print(img[100][100])

#    baris ke 1-100 akan di acak warnanya
for i in range(100) :
    for j in range(img.shape[1]) :
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

#    nge-slice gambar dan dicopy lalu dipindah ke tempat lain
head = img[90:290, 400:600]
img[50:250, 100:300] = head

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

