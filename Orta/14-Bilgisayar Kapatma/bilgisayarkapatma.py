import time
import os
t = int(input("Geri Sayım Kaç Saniye Olsun: "))
while t:
    dakika, saniye = divmod(t, 60)
    timer = f'{dakika}:{saniye}'
    print(timer, end="\r")
    time.sleep(1)
    t=t-1
    if timer=='0:1':
        print("Saniye Doldu")
        time.sleep(1)
        os.system('shutdown -s -t 0')
