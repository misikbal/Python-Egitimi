import json
import time
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
