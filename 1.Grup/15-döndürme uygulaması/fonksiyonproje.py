# # def yazdır(ad):
# #     print("Merhaba", ad)
# # isim=input("lutfen isminizi giriniz: ")
# # yazdır(isim)
# # def topla(a,b):
# #     return a+b
# # print(topla(2,3))
import time
print("X Bankasına hoşgeldiniz")
print("""
      1) Para yatır
      2) Para çek
      3) Bakiye sorgulama
      4) Çıkış      
""")
bakiye=1000
while True: 
    işlem=int(input("işlem seçiniz: "))
    if işlem==1:
        miktar=int(input("Ne kadar para yatıracaksınız"))
        bakiye=bakiye+miktar
        print("yatırılan para: ",miktar)
        print("Bakiyeniz: ",bakiye)
    elif işlem==2:
        miktar=int(input("Ne kadar para çekeceksiniz"))
        if miktar>bakiye:
            print("bakiyeniz yetersiz")
        else:
            bakiye=bakiye-miktar
            print("çekilen para: ",miktar)
            print("Bakiyeniz: ",bakiye)
    elif işlem==3:
        print("Bakiyeniz: ",bakiye)
    elif işlem==4:
        break
    else:
        print("geçersiz işlem girdiniz")
    time.sleep(2)
from datetime import date
doğumtarihi=date(2023,3,16)
bugün=date.today()
işlem=doğumtarihi-bugün
print(işlem.days)
