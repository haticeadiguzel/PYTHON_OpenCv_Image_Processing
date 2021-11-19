import cv2
import numpy as np

resim = np.zeros((300,300,3),dtype = "uint8")

cv2.line(resim, (0,20), (300,20), (0,0,225), 3)
#kaynak, nerden başlicak, nereye kadar, renk, kalınlık
#bir çizgi çizmeye yarar

cv2.circle(resim, (150,150), 25, (0,255,0), 2)
#kaynak, merkez, yarıçap, renk, kalınlık
#bir çember çizmeye yarar

cv2.putText(resim, "HelloWorld!", (50,220), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 1)
#kaynak, metin, nereden başlicak, yazı tipi, yazı boyutu, renk, kalınlık

cv2.imshow("Deneme line ", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()