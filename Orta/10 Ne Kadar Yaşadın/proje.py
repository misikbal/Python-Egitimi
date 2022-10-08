import datetime
yil=int(input("Doğum Yılınızı Giriniz: "))
ay=int(input("Doğum Ayınızı Giriniz: "))
gun=int(input("Doğum Gününüzü Giriniz: "))
dogumtarihi=datetime.date(yil,ay,gun)
bugun=datetime.date.today()
islem=bugun-dogumtarihi

print(f"""

{islem.total_seconds()} Saniye Yaşamışsın
{islem.days} Gün Yaşamışsın
{round((islem.days/7),1)} "Hafta Yaşamışsın
{round((islem.days/30),1)} Ay Yaşamışsın
{round((islem.days/365),1)} Yaşındasın
""")
