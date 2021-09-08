import cv2
import numpy as np

resim = cv2.imread("kus.jpg")

cv2.imshow("Kus", resim)

#print(resim)
#her bir pikselin matrixlerini ekrana getirir

print(resim.size)
#Görselin boyutunu ekrana yazdırır

print(resim.dtype)
#Hangi tip olduğunu ekrana getirir

print(resim.shape)
#Resmin boyutlarının değerlerini verir. Genişlik, yükseklik, kaç kanal var

resim2 = cv2.imread("kus.jpg", 0)
cv2.imshow("Kus2", resim2)
#print(resim2)
print(resim2.size)
print(resim.dtype)
print(resim.shape)
#Görseli siyah beyaz yaparsak boyutunda ve kanalında değişme meydanna gelir

cv2.waitKey(0)
cv2.destroyAllWindows()