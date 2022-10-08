import json
import time
data= open("veritabani.json","r",encoding="utf-8")
jsonformati=json.loads(data.read())

while True:
    secim=input("""
    [1] Müdür Giriş Sayfası
    [2] Öğretmen Giriş Sayfası
    [3] Öğrenci Giriş Sayfası  
    Seçiminizi Yapınız: 
    """)
    if secim=="1":
        print("Müdür Giriş Sayfası")
        kullanıcıadi=input("Kullanıcı Adınız: ")
        sifre=input("Şifreniz: ")
        dogrukullaniciadi=jsonformati["mudur"]["kullaniciad"]
        dogrusifre=jsonformati["mudur"]["sifre"]
        if kullanıcıadi==dogrukullaniciadi and sifre==dogrusifre:
            print(jsonformati["mudur"]["isim"]," Hoşgeldin")
            while True:
                mudursecim=input("""
                (1) Öğrenci Ekle
                (2) Öğretmen Ekle
                Seçiminizi Yapınız: 
                """)
                if mudursecim=="1":
                    isim=input("Öğrencini İsmi: ")
                    kullanici=input("Öğrenicinin Kullanıcı Adı: ")
                    sifre=input("Öğrencinin Şifresi: ")
                    yeniveri={
                            "numarası":jsonformati["ogrenci"][-1]["numarası"]+1,
                            "isim":isim,
                            "dersler":[],
                            "kullaniciad":kullanici,
                            "sifre":sifre
                        }
                    with open("veritabani.json","w",encoding="utf-8") as veri:
                        json.insert(
                            veri,
                            yeniveri
                        )
                        
        else:
            print("Hatalı Giriş")
            time.sleep(1)



