from random import randint
print("Web Sitesine Hoşgeldiniz.")
dogrumail="ikbal.sirdas@gmail.com"
dogrusifre="12345678"
hak=3
while True:
    print("""
    [1] Giriş Yap
    [2] Şifremi Unuttum
    """)
    secim=input("Seçim Yapınız: ")
    if secim=="1":
        if hak==0:
            print("Hatalı Giriş Sorun Var")
            break
        else:
            print(f"{hak} hakkınız kaldı")
            mail=input("E-posta Adresinizi Giriniz:")
            parola=input("Şifrenizi Giriniz: ")
            if dogrumail==mail and dogrusifre==parola:
                print("Hoşgeldiniz Giriş Yaptınız")
                break
            else:
                hak=hak-1
                print("""Mail adresiniz veya 
                parola yanlış""")
    elif secim=="2":
        kod=randint(1000,9999)
        print(kod)