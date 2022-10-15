
import requests
api="d67be9e3d6656e4045320d35e17c72ca"
sehir=input("Bir Şehir Giriniz: ")
url="http://api.openweathermap.org/data/2.5/weather?appid="+api+"&q="+sehir
havadurumu=requests.get(url).json()
print(havadurumu)