from datetime import date
d1 = date(2023, 6, 23)
y2k = date.today()
diff = d1 - y2k
days = diff.days
print(days)