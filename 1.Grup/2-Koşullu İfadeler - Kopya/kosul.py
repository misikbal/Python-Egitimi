# kısa yollar
#toplum yorum= ctrl+K+C
# toplu yorumdan çıkarma ctrl+K+U
# kopyalama ctrl+c
# yapıştırma ctrl+v
# yapılan işlemi geriye alma ctrl+z
# yapılan işlemi ileriye alma ctrl+y





print("1-)Girilen sayının pozitif, negatif, sıfır olduğunu bulan proje")
deger=int(input("Bir sayı giriniz: ")) 
#burada kullanıcından veri alıyoruz 
# int() fonksiyonu metinsel değerleri sayısal değere dönüştürür. 
# input'un varsayılan değeri string olduğundan int() fonksiyonu kullanırız.
if deger<0:
    print("Negatif")
elif deger>0:
    print("Pozitif")
elif deger==0:
    print("Sıfır")
#Üç koşul olduğu için teker teker kontrol ediyoruz.
# Burada dikkat edilmesi gerek nokta deger ifadesinin sıfıra eşit olduğunu söyleyebilmek için iki eşittir (==) kullanıyoruz.
# Girintiler çok önemli girinti içerisine yazılmazsa o kod yazılmayacaktır.
# Bu bir yazım kuralıdır. Bir tab (yani dört boşluk) içeri alıyoruz

print("2-)Girilen sayının tek mi çift mi olduğunu bulan proje")
deger2=int(input("Bir sayı giriniz: "))
if deger2%2==0:
    print("Sayı çift")
if deger2%2!=0:
    print("Sayı tek")
# % işareti mod almaya yarıyor.
# Mod alma işlem nedir diyecek olursanız. 
# Bir sayının ikiye böldüğünüzde kalan sayıyı veren işleme mod diyoruz.
# Mod alma işlemi sayının kalanını verir.
# Bir sayının çift olup olmadığını anlayabilmek için o sayıyı 2 ye böler ve kalanı 1 ise tek, 0 ise çift olarak kabul edilir.


print("3-)basit login projesi 1.yol")
dogruEmail="ikbal.sirdas@gmail.com"
dogruSifre="12345"
kullanıcıEmail=input("Email Adresinizi Giriniz: ")
kullanıcıSifre=input("Şifrenizi Giriniz: ")
if dogruEmail==kullanıcıEmail:
    if dogruSifre==kullanıcıSifre:
        print("Hoşgeldiniz")
    else:
        print("Şifreniz yanlış")
else:
    print("Email yanlış")


print("4-)basit login projesi 2.yol")
dogruEmail="ikbal.sirdas@gmail.com"
dogruSifre="12345"
kullanıcıEmail=input("Email Adresinizi Giriniz: ")
kullanıcıSifre=input("Şifrenizi Giriniz: ")
#yukarıdaki örnek ile bu örnek aynı. Sadece tek fark and operatörünü kullanarak iç içe koşul yazmak yerine tek koşul yazmamıza olanak sağlıyor.
#ÖNEMLİ NOT!! Bir projede ne kadar az if else yani koşul var ise o proje o kadar kaliteli ve performanslıdır.
if dogruEmail==kullanıcıEmail and dogruSifre==kullanıcıSifre:
    print("Hoşgeldiniz")

else:
    print("Email yanlış")


#Vücut kitle indeks hesaplama formülü : Kilo / boyun karesidir
print("5-)Kilo indeks hesaplama projesi")
boy=float(input("Metre Cinsinden Boyunuzu Giriniz (172cm=1.72): "))
kilo=int(input("Kilonuzu Giriniz: "))
sonuc=kilo/boy**2
#iki çarpı koyunca o sayının üssünü alıyoruz.

print(sonuc)

if sonuc<18.4:
    print("Zayif Birisiniz.")
elif sonuc>18.5 and sonuc<24.9:
    print("Normal Bir Kilon var")
elif sonuc>25 and sonuc<29.9:
    print("Fazla Kilolu Birisiniz.")
elif sonuc>30 and sonuc<34.9:
    print("Şişman (Obez) - I. Sınıf")
elif sonuc>35 and sonuc<44.9:
    print("Şişman (Obez) - II. Sınıf")
elif sonuc>45:
    print("Aşırı Şişman (Aşırı Obez) - III. Sınıf")