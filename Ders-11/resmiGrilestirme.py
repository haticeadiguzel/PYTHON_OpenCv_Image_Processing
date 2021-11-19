import cv2
import numpy as np

resim = cv2.imread("nataliePortman.jpg")

resimGri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
#resmi grileştirmek için kullanılır. Böylece boyut küçülür.

yukseklik,genislik,kanalSayisi = resim.shape
yukseklik,genislik = resimGri.shape
#Çoklu tanımlama. Sahape ten aldığımız verileri parametrelere atar
#grileştirilende kanal sayısı yazılmaz çünkü kanalı yoktur

print("Original: ", yukseklik, genislik, kanalSayisi)
print("Gri: ", yukseklik, genislik)

cv2.imshow("Natalie Portman" ,resim)
cv2.imshow("Gri Natalie Portman", resimGri)

cv2.waitKey(0)
cv2.destroyAllWindows()