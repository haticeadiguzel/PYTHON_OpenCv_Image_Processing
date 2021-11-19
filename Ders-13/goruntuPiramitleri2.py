import cv2
import numpy as np

resim = np.zeros((300,300,3), dtype = "uint8")
#shape oluşturduk, data type
#zeros numpy de bir sınıftır. bir matris döndürür. boyutları kanalları ve değerleri gireriz.

print(resim)

cv2.waitKey(0)
cv2.destroyAllWindows()