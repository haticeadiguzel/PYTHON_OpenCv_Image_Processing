import cv2
import numpy as np

resim = cv2.imread("Kemal_sunal.jpg")

resim[:,:,0] = 50
resim[:,:,1] = 200
#blue'ya erişim sağlayıp 255 atadık. Efect
#0 = blue, 1 = green, red = 2
#tüm resme efekti ekler

resim[30:50,60:900,2] = 255
#sadece belirli bir alana efekt uygular

cv2.imshow("Kemal Sunal", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()