import cv2
import numpy as np

resim = cv2.imread("adileNasit.jpg")

aynalama = cv2.copyMakeBorder(resim, 75, 75, 125, 125, cv2.BORDER_REFLECT)
#resmi aynalar. resim adı, boyutları, istediğimiz özellik

uzatma = cv2.copyMakeBorder(resim, 120, 120, 120, 120, cv2.BORDER_REPLICATE)
#resmi uzatır

tekrarlama = cv2.copyMakeBorder(resim, 300, 300, 300, 300, cv2.BORDER_WRAP)
#resmi tekrarlar

sarma = cv2.copyMakeBorder(resim, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value = (0,0,255))
#resmi sarar

cv2.imshow("Adile Nasit Aynalama", aynalama)

cv2.imshow("Adile Nasit Uzatma", uzatma)

cv2.imshow("Adile Nasit Tekrarlama", tekrarlama)

cv2.imshow("Adile Nasit Sarma", sarma)





cv2.waitKey(0)
cv2.destroyAllWindows()