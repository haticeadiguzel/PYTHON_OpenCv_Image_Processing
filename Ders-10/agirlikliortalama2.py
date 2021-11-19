import cv2
import numpy as np

resim1 = cv2.imread("cemyilmaz.jpg")
resim2 = cv2.imread("ozanguven.jpg")

cv2.imshow("Cem yilmaz", resim1)
cv2.imshow("ozan guven", resim2)

toplam = cv2.add(resim1, resim2)
#iki resmi üst üste alır. Resimlerin boyutları aynı olmak zorundadır

agirliklitoplama = cv2.addWeighted(resim1, 0.7, resim2, 0.3, 0)
#iki resmin saydamlıklarıyla oynayarak üst üste alır.
# ilk resim, saydamlık, ikinci resim, saydamlık, herzaman sıfır. Saydamlıklar toplamı 1 etmek zorunda

cv2.imshow("Toplam", toplam)
cv2.imshow("agirlikli toplama", agirliklitoplama)

cv2.waitKey(0)
cv2.destroyAllWindows()