from datetime import date
sinavtarihi = date(2023, 6, 23)
bugun = date.today()
sonuc = sinavtarihi - bugun
days = sonuc.days
print(days)



