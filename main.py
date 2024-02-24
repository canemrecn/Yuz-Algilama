import cv2
#Gerekli kütüphaneyi import et
yuzCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
# Yüz tanıma sınıflandırıcısını yükle
kamera = cv2.VideoCapture(0)
# Kamera bağlantısını başlat
while True:
    _, kare = kamera.read()
 # Bir kareyi oku
    gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
# Kareyi gri tonlamalı görüntüye dönüştür
    yuzler = yuzCascade.detectMultiScale(
        gri,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (20, 20)
    )
# Yüzleri tespit et
    for (x,y,w,h) in yuzler:
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),2)
# Tespit edilen yüzleri dikdörtgenle çerçevele
    cv2.imshow('kare',kare)
# Kareyi göster
    k = cv2.waitKey(1) & 0xff
# Klavyeden bir tuşa basılmasını bekle
    if k == 27 or k == ord('q'):
        break
# ESC veya 'q' tuşuna basıldığında döngüyü sonlandır
kamera.release()
# ESC veya 'q' tuşuna basıldığında döngüyü sonlandır
cv2.destroyAllWindows()
# Tüm pencereleri kapat