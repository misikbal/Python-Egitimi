import time
print("Bankamatik Uygulaması")
bakiye=1000
dolar=100
euro=50
while True:
    islem=input("""
    (1) Bakiye Görüntüle
    (2) Para Çek
    (3) Para Yatır
    Yapılacak işlemin numarasını yazınız?
    """)

    if islem=="1":
        print("Bakiyeniz:",bakiye,"TL")
        print("Bakiyeniz:",dolar,"USD")
        print("Bakiyeniz:",euro,"EUR")
        time.sleep(2)
    elif islem=="2":
        para=input("Ne Kadar Para Çekmek İstersiniz?")
        para=para.split(" ")
        
        if para[1]=="TL":
            para=int(para[0])
            if bakiye>=para:
                bakiye=bakiye-para
                print("Kalan Paranız:",bakiye)
            else:
                print("Yetersiz Bakiye")
                print("Kalan Paranız:",bakiye)
        

        elif para[1]=="USD":
            para=int(para[0])
            if dolar>=para:
                dolar=dolar-para
                print("Kalan Paranız:",dolar)
            else:
                print("Yetersiz Bakiye")
                print("Kalan Paranız:",dolar)
        

        elif para[1]=="EUR":
            para=int(para[0])
            if euro>=para:
                euro=euro-para
                print("Kalan Paranız:",euro)
            else:
                print("Yetersiz Bakiye")
                print("Kalan Paranız:",euro)
        time.sleep(2)
    elif islem=="3":
        para=int(input("Ne kadar para yatıracaksınız? "))
        bakiye=bakiye+para
        print("Bakiyeniz: ",bakiye)
        time.sleep(2)

