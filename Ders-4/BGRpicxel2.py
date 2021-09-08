import cv2
import numpy as np

resim = cv2.imread("joker.jpg")

resim[50,30] = [255,255,255]
#istediğimiz bir pixceli başka bir renk ile değiştirdik

for i in range(100):
    resim[70, i] = [255,255,255]
    #Belli bir kısmı değiştirmek için kullandık

cv2.imshow("Joker", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
