#Python Listeleri Öğrenelim
"""Listeler oldukça yararlı ve 
fonksiyonel bir Python değişken türüdür. 
Kullanım amaçları bir veri topluluğunu tek 
çatı altında toplayarak kolay ulaşılabilir
hale getirmektir. Üstelik aynı stringler 
gibi ,indekslenir,parçalanır ve işlemlere 
tabi tutulabilirler. Bu sayede ortak veya 
ortak olmayan kümeler halinde bir araya 
getirebileceğiniz verileri aşağıda 
örneklerini göreceğiniz birçok fonksiyon 
ile kullanabilir ve birçok işleme tabi 
tutabilirsiniz."""
# Python array değişken türünün en önemli
# özelliklerinden birisi dizi içinde farklı 
# değişken türlerini bir arada tutabilmenizdir.
# Böylece oldukça kolay bir şekilde farklı 
# türleri aynı dizide depolayabilirsiniz. 
# Öyleyse birçok farklı yöntemle liste/dizi 
# nasıl oluşturulur hemen onu görelim.

# for,while,forEach

# boş liste değişkeni 
liste =  []

# dizi/liste(array) oluşturmanın farklı bir tarzı
liste =  list()

# sadece int değerler tutan dizi/liste
liste =  [1,2,3,4,5,6,7]

# string tutan array
liste =  list("İstanbul","Ankara","İzmir")


# farklı değişken türleri tutan liste isimli array değişkeni
liste =  [10,11,12,"Python",3.14,51.035]

# string parçalayarak dizi/liste oluşturma
isim = "Python Kursu"
liste =  list(isim)
# >>> ['P','y','t','h','o','n',' 
# ','K','u','r','s','u'] 
# // yukarıdaki işlem sonucu oluşan dizi,

# array indexleme /basit dizi
liste = ["Elma","Armut","Kivi","Muz"]
liste[2]

# >>> "Kivi"


# sayilar = [1,2,3,4,5]
# for sayi in sayilar:
#    print(sayi)

# isimler = ['çınar','sadık','sena']
# for isim in isimler:
#     print(f'my name is {isim}')

# sayilar = [1,3,5,7,9,12,19,21]

# Sayilar listesindeki hangi sayılar 3' ün 
# katıdır ?

# for sayi in sayilar:
#    if (sayi%3==0):
#        print(sayi)

# Sayilar listesinde sayıların toplamı kaçtır ?

# toplam = 0
# for sayi in sayilar:
#     toplam += sayi
# print('toplam:',toplam)

# Sayilar listesindeki tek sayıların karesini alınız.

# for sayi in sayilar:
#    if (sayi % 2 == 1):
#       print(sayi ** 2)

# Şehirlerden hangileri en fazla 5 karakterlidir ?

# sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# for sehir in sehirler:
#    if (len(sehir) <= 5):
#       print(sehir)

