import cv2
import numpy as np

camera = cv2.VideoCapture(0)
#0 dersek kendi bilgisayarımızın kamerasını alır.
#1 dersek USB ye bağlı kamerayı çalıştırır.
#2 dersek buraya yerleştirilmiş videoda kullanılır.

while True:

    ret, goruntu = camera.read()
    #Kameranın çalışıp çalışmadığını kontrol eder.
    #videolar görüntülerin kısa aralıklarla çekilip birleştirilmesiyle oluşur bu yüzden loop kullanırız.
    
    cv2.imshow("Kameranın goruntusu", goruntu)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    #30 milisaniyede bir görüntüleri çek ve birleştir. çıkmak için q ya bas.
    #0xFF çıkmak demek

camera.release()
#kamerayı serbest bırakırız.

#cv2.waitKey(0)
#kullanmadık çünkü q ya bastıktan sonra kamera kapanmıyor ve donuyor.
cv2.destroyAllWindows()