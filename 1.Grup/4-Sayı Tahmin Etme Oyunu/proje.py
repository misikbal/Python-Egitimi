from random import randint
sayi=randint(1,10)
hak=3
for i in range(1,4):
    print(f"{hak} hakkınız kaldı")
    if hak==0:
        print("Game Over")
        break
    else:
        tahmin=int(input("Tahmininizi Giriniz: "))
        if tahmin==sayi:
            print("Tebrikler bildiniz")
            break
        elif tahmin>sayi:
            print("Daha küçük bir sayı giriniz")
        elif tahmin<sayi:
            print("Daha büyük bir sayı giriniz")
        hak=hak-1