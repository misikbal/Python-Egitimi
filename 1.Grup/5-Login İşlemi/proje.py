from random import randint
dogrumail="@mail"
dogrusifre="123"
hak=3
while True:
    print("""
    [1] Giriş Yap
    [2] Şifremi Unuttum
    """)
    secim=input("Seçiminizi Yapınız: ")
    if secim=="1":
        if hak==0:
            print("Hacker başaramadın :)")
            break
        else:
            mail=input("Email Adresini Gir: ")
            sifre=input("Şifreni Gir: ")
            if mail==dogrumail and sifre==dogrusifre:
                print("Hoşgeldiniz.")
                break
            else:
                hak=hak-1
                print(f"{hak} hakkınız kaldı")
                print("E-mail veya parola yanlış")

    elif secim=="2":
        kod=randint(1000,9999)
        print(f"{dogrumail} dört haneli kod {kod} gönderildi")
        kullanicikod=int(input("Kodu Giriniz: "))
        if kullanicikod==kod:
            print("Kod Doğru")
            yenisifre=input("Yeni sifrenizi giriniz:")
            dogrusifre=yenisifre
        else:
            print("Kod yanlış")
            break