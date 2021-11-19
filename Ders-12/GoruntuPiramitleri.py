import cv2
import numpy as np

resim = cv2.imread("nataliePortman.jpg")
ikiKat = cv2.pyrUp(resim)
#büyültmek iki kat yapmak için kullanılır
yarisi = cv2.pyrDown(resim)
#küçültmek için kullanılır. yarısına getirir

print("Orijinal: " , resim.shape)
print("Buyutulmus: " , ikiKat.shape)
print("Kucultulmus: " , yarisi.shape)

cv2.imshow("orijinal resim", resim)
cv2.imshow("iki kat buyuk resim", ikiKat)
cv2.imshow("Yarisi", yarisi)

cv2.waitKey(0)
cv2.destroyAllWindows()