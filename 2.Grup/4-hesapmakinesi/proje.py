while True:

    sayi1=int(input("Birinci Sayınız Giriniz: "))
    sayi2=int(input("İkinci Sayınız Giriniz: "))

    islem=input("""
    Toplama(+)
    Çıkarma(-)
    Çarpma(*)
    Bölme(/)
    Üs Alma(**)
    Yapmak istediğiniz işlemin simgesini giriniz: 
    """)

    if islem=="+":
        print("""Toplama 
        İşleminizin 
        Sonucu: """
        +str(sayi1+sayi2))
    elif islem=="-":
        print("Çıkarma İşleminizin Sonucu: "+sayi1-sayi2)
    elif islem=="*":
        print("Çarpma İşleminizin Sonucu: "+str(sayi1*sayi2))
    elif islem=="/":
        print("Bölme İşleminizin Sonucu: "+sayi1/sayi2)
    elif islem=="**":
        print("Üs Alma İşleminizin Sonucu: "+sayi1**sayi2)

    sonuc=input("""Devam Etmek için (e) tuşuna, 
    çıkmak içim (ç) basınız: """)
    if sonuc=="ç":
        break
    elif sonuc=="e":
        continue
    else:
        print("Yanlış tuşlama yaptınız. Lütfen tekrar deneyiniz.")


