import time
print("Miyonlar Bankasına Hoşgeldiniz")

bakiye=1000
while True:
    
    print("""
    1- Para Yatır
    2- Para Çek
    3- Bakiye Sorgulama
    4- Çıkış
    """)
    islem=int(input("İşlem Seçiniz: "))
    if islem==1:
        miktar=int(input("Kaç Para Yatıracaksınız?"))
        bakiye=bakiye+miktar
        print("Yatırılan Para: ",miktar)
        print("Bakiyeniz: ",bakiye)
    elif islem==2:
        miktar=int(input("Kaç Para Çekeceksiniz?"))
        if miktar>bakiye:
            print("Bakiyeniz yetersiz")
        else:
            bakiye=bakiye-miktar
            print("Çekilen Para: ",miktar)
            print("Bakiyeniz: ",bakiye)
    elif islem==3:
        print("Bakiyeniz: ",bakiye)
    elif islem==4:
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz İşlem")
    time.sleep(2)