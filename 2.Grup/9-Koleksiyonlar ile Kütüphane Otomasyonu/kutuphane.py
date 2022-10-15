kitaplar=[
    {
    "isim":"Beyaz Gemi",
    "yazar":"Cengiz Aytmatov",
    "sayfaSayısı":168,
    "yılı":1995
    },
    {
    "isim":"Serenad",
    "yazar":"Zülfü Livaneli",
    "sayfaSayısı":450,
    "yılı":2016
    }
]   




while True:
    yapilacak=input("""
        (1) Kitap Ekleme
        (2) Kitap Arama
        (3) Kitap Silme
        (4) Tüm Kıtapları Görüntüle
    """)
    if yapilacak=="1":
        print("Kitap Ekleme Sayfası")
        kitapadi=input("Kitap Adı: ")
        kitapyazar=input("Kitabın Yazarı: ")
        kitapsayafasi=int(input("Kitabın Toplam Sayfası:"))
        kitapyili=int(input("Kitabın Yılı: "))
        kitaplar.append({
            
            "isim":kitapadi,
            "yazar":kitapyazar,
            "sayfaSayısı":kitapsayafasi,
            "yılı":kitapyili
            
            })
    elif yapilacak=="2":
        print("Kitap Arama Sayfası")
        arama=input("Hangi Kıtabı Arıyorsun: ")
        for i in kitaplar:
            if arama==i["isim"]:
                print(i["isim"]," Kıtabı Var")

    elif yapilacak=="3":
        print("Kitap Silme Sayfası")
        silinecek=input("Hangi Kitabı Silmek İstersin: ")
        for i in kitaplar:
            if silinecek==i["isim"]:
                kitaplar.pop(kitaplar.index(i))
                print(silinecek, "Kitabı Silindi.")

    elif yapilacak=="4":
        print("Kütüphanedeki Tüm Kitaplar")
        for i in kitaplar:
            print(i["isim"])



