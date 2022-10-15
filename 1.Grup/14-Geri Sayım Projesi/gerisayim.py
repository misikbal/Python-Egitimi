import time
import os
t=int(input("Geri Sayım İçin Saniyenizi Giriniz: "))

while t:
    dakika,saniye=divmod(t,60)
    sonuc=f"{dakika}:{saniye}"
    print(sonuc,end="\r")
    time.sleep(1)
    t=t-1
    if sonuc=="0:1":
        print("Geri Sayım Bitti")
        print("Bilgisayar Kapatılıyor...")
        time.sleep(2)
        os.system("shutdown -s -t 0")