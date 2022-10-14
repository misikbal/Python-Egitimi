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
        dogrukullaniciadi=jsonformati["mudur"]["kullanıcıadı"]
        dogrusifre=jsonformati["mudur"]["şifre"]
        if kullanıcıadi==dogrukullaniciadi and sifre==dogrusifre:
            print(jsonformati["mudur"]["adı"]," Hoşgeldin")
            while True:
                mudursecim=input("""
                (1) Öğrenci Ekle
                (2) Öğretmen Ekle
                (3) Tüm Öğrencileri Görüntüle
                (4) Tüm Öğretmenleri Görüntüle
                Seçiminizi Yapınız: 
                """)
                if mudursecim=="1":
                    isim=input("Öğrencini İsmi: ")
                    kullanici=input("Öğrenicinin Kullanıcı Adı: ")
                    sifre=input("Öğrencinin Şifresi: ")
                    yeniveri={
                            "numarası":jsonformati["öğrenci"][-1]["numarası"]+1,
                            "adı":isim,
                            "dersler":[],
                            "kullanıcıadı":kullanici,
                            "şifre":sifre
                        }
                    with open("veritabani.json","r+",encoding="utf-8") as veri:
                        jsonveri=json.load(veri)
                        jsonveri["öğrenci"].append(yeniveri)
                        veri.seek(0)
                        json.dump(jsonveri,veri,indent=4)
                        print("Öğrenci Başarıyla Eklendi")
                        time.sleep(1)

                if mudursecim=="2":
                    isim=input("Öğretmenin İsmi: ")
                    kullanici=input("Öğretmenin Kullanıcı Adı: ")
                    sifre=input("Öğretmenin Şifresi: ")
                    brans=input("Öğretmenin Branşı: ")
                    yeniveri={
                            "adı":isim,
                            "kullanıcıadı":kullanici,
                            "şifre":sifre,
                            "branş":brans
                        }
                    with open("veritabani.json","r+",encoding="utf-8") as veri:
                        jsonveri=json.load(veri)
                        jsonveri["öğretmen"].append(yeniveri)
                        veri.seek(0)
                        json.dump(jsonveri,veri,indent=4)
                        print("Öğretmen Başarıyla Eklendi")
                        time.sleep(1)




            #     with open("kitaplar.json","r+",encoding="utf-8") as veriler:
            # jsonfile=json.load(veriler)
            # jsonfile["kitap"].append(yeniveri)
            # veriler.seek(0)
            # json.dump(jsonfile,veriler,indent=4)
        else:
            print("Hatalı Giriş")
            time.sleep(1)



