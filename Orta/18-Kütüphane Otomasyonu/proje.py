import json
import time
import datetime
def kitapokuma():
    with open("kitaplar.json","r",encoding="utf-8") as kitap:
        jsonformati=json.loads(kitap.read())
        return jsonformati


while True:
    secim=input("""
    (1) Tüm Kitapları Görüntüle
    (2) Kitap Ekle
    (3) Kitap Sil
    (4) Kitap Ver
    (5) Kitap Teslim Al
    
    Seçiminizi Yapınız:
    """)
    if secim=="1":
        
        print("Tüm Kitapları Görüntüleme Sayfası")
        siranumarasi=0
        for i in kitapokuma()["kitap"]:
            
            print(f"""
    --------------------
    Kitap Adı:{kitapokuma()["kitap"][siranumarasi]["isim"]}
    Kitabın Yazarı:{kitapokuma()["kitap"][siranumarasi]["yazar"]}
    Kitabın Durumu:{kitapokuma()["kitap"][siranumarasi]["durum"]}

    --------------------
            """)
            siranumarasi+=1
        time.sleep(3)
    elif secim=="2":
        print("Kitap Ekleme Sayfası")
        kitapadi=input("Kitap Adı: ")
        kitapyazar=input("Kitabın Yazarı: ")
        kitapsayfa=int(input("Kitabın Sayfası: "))
        kitapyili=int(input("Kitabın Basım Yılı: "))
        kitapdurum=bool(input("Kitabın Durumu: "))
        yeniveri={
            "id":kitapokuma()["kitap"][-1]["id"]+1,
            "isim":kitapadi,
            "yazar":kitapyazar,
            "sayfa":kitapsayfa,
            "yılı":kitapyili,
            "durum":kitapdurum
        }
        
        with open("kitaplar.json","r+",encoding="utf-8") as veriler:
            jsonfile=json.load(veriler)
            jsonfile["kitap"].append(yeniveri)
            veriler.seek(0)
            json.dump(jsonfile,veriler,indent=4)
        print("Kitap Başarıyla Eklendi")
        time.sleep(1)
    

    elif secim=="3":
        print("Kitap Silme Sayfası")
        secim=input("Tüm Kitaplar Görüntülensin mi?")
        if secim=="evet":
            print("Tüm Kitapları Görüntüleme Sayfası")
            siranumarasi=0
            for i in kitapokuma()["kitap"]:
                
                print(f"""
        --------------------
        {kitapokuma()["kitap"][siranumarasi]["id"]} - {kitapokuma()["kitap"][siranumarasi]["isim"]}
        --------------------
                """)
                siranumarasi+=1
            silinecek=int(input("Kaç Numralı Kitabı Silme İstersiniz: "))
            sayi=0
            for i in kitapokuma()["kitap"]:
                if silinecek==i["id"]:
                    kitapokuma()["kitap"].pop(sayi)
                sayi+=1
                
        else:
            continue
        
        
        
        # with open("kitaplar.json","r+",encoding="utf-8") as file:
        #     file_data = json.load(file)
        #     file_data["kitap"].append(yeniveri)
        #     file.seek(0)
        #     json.dump(file_data,file,indent=4)




