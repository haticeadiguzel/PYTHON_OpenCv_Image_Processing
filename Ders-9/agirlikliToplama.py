import cv2
import numpy as np

#Resim1 = [200,100,50]
#Resim2 = [100,50,210]
#Resim1 + Resim2 = [45,150,5]

resim1 = cv2.imread("emelsayin.jpg")
resim2 = cv2.imread("turkansoray.jpg")

print(resim1[50,100])
print(resim2[100,200])

cv2.imshow("Emel SAYIN", resim1)
cv2.imshow("Turkan SORAY", resim2)

print(resim1[50,100] + resim2[100,200])

cv2.waitKey(0)
cv2.destroyAllWindows()