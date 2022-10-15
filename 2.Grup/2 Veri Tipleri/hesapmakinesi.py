while True:
    sayi1=input("Birinci Sayınızı Giriniz: ")
    sayi2=input("İkinci Sayınızı Giriniz: ")
    hesaplanacak=input("""
    [1] - Toplama
    [2] - Çıkarma
    [3] - Çarpma
    [4] - Bölme
    Hesaplanacak işlemi seçiniz: 
    """)

    if hesaplanacak=="1":
        print(int(sayi1)+int(sayi2))
    elif hesaplanacak=="2":
        print(int(sayi1)-int(sayi2))
    elif hesaplanacak=="3":
        print(int(sayi1)*int(sayi2))
    elif hesaplanacak=="4":
        print(int(sayi1)/int(sayi2))
    else:
        print("Geçersiz işlem seçtiniz")
    devam=input("Devam etmek için [e], Çıkmak İçin [ç] tuşuna basınız")
    if devam=="e":
        continue
    elif devam=="ç":
        break