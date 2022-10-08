import random
import string

def sifre_olusturucu(uzunluk,zorluk_seviyesi,olusturulan_sifre=[]):
    karakterler=string.ascii_letters
    if zorluk_seviyesi==1:
        karakterler=string.ascii_lowercase
        print(karakterler)
    elif zorluk_seviyesi==2:
        karakterler=string.ascii_letters+string.digits
        print(karakterler)
    elif zorluk_seviyesi==3:
        karakterler=string.ascii_letters+string.digits+string.punctuation
        print(karakterler)
    for i in range(uzunluk):
        olusturulan_sifre.append(random.choice(karakterler))
    return "".join(olusturulan_sifre)


uzunluk=int(input("Sifre uzunlugunu giriniz: "))
zorluk=int(input("Zorluk seviyesini giriniz: "))
print(f" Sizin için oluşturduğum Şifre : \n {sifre_olusturucu(uzunluk,zorluk)}")