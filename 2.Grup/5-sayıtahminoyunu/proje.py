from random import randint

rand = randint(1, 10)
hak=3
for i in range(1,4):
    print(f"{hak} hakkınız kaldı")
    tahmin = int(input(f"{i}.Hakkınz için bir sayı giriniz: "))
    if hak==0:
        print("Game Over")
    else:
        
        if tahmin == rand:
            print("Tebrikler bildiniz")
            break
        elif tahmin > rand:

            print("""Daha küçük bir sayı giriniz""")
        elif tahmin < rand:
            print("Daha büyük bir sayı giriniz")
    hak=hak-1
    
    # elif tahmin!=rand:
    #     print("Tahmininiz yanlış")
    #     continue
    # ctrl+k+c



