import requests
Api_key='d67be9e3d6656e4045320d35e17c72ca'
city=input("Şehir Giriniz: ").lower()
base_url="http://api.openweathermap.org/data/2.5/weather?appid="+Api_key+"&q="+city
weather_data=requests.get(base_url).json()
print(round(weather_data["main"]["temp"]-273,2))