import cv2
import numpy as np

resim = cv2.imread("kurt.jpg")

cv2.imshow("Kurt", resim)

print(resim[(230,80)])
#Belirtilen noktayı alır ve bgr değerini verir

print("Resmin boyutu: " + str(resim.size))
#str çevirerek string ile yazabildik

cv2.waitKey(0)
cv2.destroyAllWindows()