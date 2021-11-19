import cv2
import numpy as np

resim = cv2.imread("Hababam.jpg")

cv2.rectangle(resim, (75,75), (115,30), [0,0,255], 1)
#resim, sol alt(önce x sonra y), sağ üst, renk, kalınlık

print(resim[50,50])
#BGR değerini verir. y ekseni x ekseni.

cv2.imshow("hababam sinifi", resim)

#Bir resimde belli bir noktayı kare içine almak istersek sol alt köşesinin
#ve sağ üst köşesinin koordinatlarını alırız.

cv2.waitKey(0)
cv2.destroyAllWindows()