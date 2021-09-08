import cv2
import numpy as np

#görseli okur. aynı dizinde olması daha iyidir
#ikinci parametre olarak 0 kullanmamız renkleri sadece siyah beyaz yapar
resim = cv2.imread("logo.png", 0)

#tanımladığımız görselin adı ile ekrana gösterir
cv2.imshow("Ozengineer Logo", resim)

#eğer oluşturduğumuz siyah beyaz resmide dosyya içine kaydetmek istersek böyle yazarız.
cv2.imwrite("logo2.png", resim)

#açıldıktan sonra kapanması için bir tuşa basılmasını gerektirir
cv2.waitKey(0)

#açıldıktan sonra kapatınca opencv ye dair her pencereyi kapatır
cv2.destroyAllWindows() 