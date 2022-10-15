import requests
import time
from datetime import datetime
import pytz
import json
from urllib.request import urlopen
import http.client

api="d67be9e3d6656e4045320d35e17c72ca"
havadurumuUrl="http://api.openweathermap.org/data/2.5/weather?appid="+api+"&q=mardin"

token="XXX"
#Bu kısmı kendi token id'nizi girmeniz gerekli gerekli açıklamayı gruba yazmıştım
url=f"https://api.telegram.org/bot{token}/sendMessage"
photourl=f"https://api.telegram.org/bot{token}/sendMessage"
chat_id="XXX"
#Bu kısmı kendi id numaranızı girmeniz gerekli gerekli açıklamayı gruba yazmıştım
depremurl="https://hasanadiguzel.com.tr/api/sondepremler"
dovizurl="https://hasanadiguzel.com.tr/api/kurgetir"
bayrak=["🇺🇸","🇦🇺","🇩🇰","🇪🇺","🇬🇧","🇨🇭","🇸🇪","🇨🇦","🇰🇼","🇳🇴","🇸🇦","🇯🇵","🇧🇬","🇷🇴","🇷🇺","🇮🇷","🇨🇳","🇵🇰","🇶🇦","🇰🇷","🇦🇿","🇦🇪","🇹🇷"]
sonsaat="16:37:50"
i=0
while True:    
    deger=urlopen(depremurl).read().decode("utf-8")
    jsonformati=json.loads(deger)
    deprem=jsonformati["data"]
    saat=deprem[0]["saat"]
    yerel = pytz.timezone("Turkey")
    simdiki = datetime.now(yerel)
    turkeysaat = simdiki.strftime("%H")
    turkeysaat2 = simdiki.strftime("%H:%M")
    if str(turkeysaat)==str(saat.split(":")[0]) and sonsaat!=saat and float(deprem[0]["ml"])>3:
        
        data2={"chat_id": f"{chat_id}","text":f"""
        {deprem[0]["ml"]} {deprem[0]["yer"]}
https://maps.google.com/?q={deprem[0]["enlem_n"]},{deprem[0]["boylam_e"]}&ll={deprem[0]["enlem_n"]},{deprem[0]["boylam_e"]}&z=8
            """}
        sonsaat=saat
        requests.post(url,data2).json()
    if str(turkeysaat2)=="08:00" or str(turkeysaat2)=="17:00" :
        deger2=urlopen(havadurumuUrl).read().decode("utf-8")
        havajson=json.loads(deger2)
        coord=havajson["coord"]
        weather=havajson["weather"][0]
        wind=havajson["wind"]
        icon="🤷‍♂️"
        if weather["icon"]=="11d":
            icon="⛈"
        elif weather["icon"]=="09d":
            icon="☔"
        elif weather["icon"]=="10d":
            icon="🌦"
        elif weather["icon"]=="13d":
            icon="❆"
        elif weather["icon"]=="50d":
            icon="🌫"
        elif weather["icon"]=="01d":
            icon="🌞"
        elif weather["icon"]=="01n":
            icon="🌜"
        elif weather["icon"]=="03d" or weather["icon"]=="03n" :
            icon="☁"
        elif weather["icon"]=="04d" or weather["icon"]=="04n" :
            icon="⛅"
        deger=urlopen(dovizurl).read().decode("utf-8")
        jsonformati=json.loads(deger)
        getdata=jsonformati["TCMB_AnlikKurBilgileri"]
        data={"chat_id": f"{chat_id}","text":f"""   
GÜNCEL DÖVİZ KURU
1 {getdata[0]["Isim"]}{bayrak[0]} = {getdata[0]["ForexSelling"]} TL 
1 {getdata[3]["Isim"]}{bayrak[3]} = {getdata[3]["ForexSelling"]} TL 
1 {getdata[4]["Isim"]}{bayrak[4]} = {getdata[4]["ForexSelling"]} TL
1 {getdata[5]["Isim"]}{bayrak[5]} = {getdata[5]["ForexSelling"]} TL

HAVA DURUMU
Bugün Mardin'de 
{weather["description"]} {icon}
En Düşük Sıcaklık: {coord["lat"]} ℃
En Yüksek Sıcaklık: {coord["lon"]} ℃
Nem: %{havajson["main"]["humidity"]}
Basınç: {havajson["main"]["pressure"]}
Rüzgar Hızı: {wind["speed"]} km/s
Rüzgar Yönü: {wind["deg"]}°
Bulut Yoğunluğu: {havajson["clouds"]["all"]}
        """}        
        requests.post(url,data).json()
        time.sleep(59)
    gun = simdiki.strftime("%A")
    if str(turkeysaat2)=="17:01" and (gun=="Monday" or gun=="Tuesday" or gun=="Wednesday" or gun=="Thursday" or gun=="Friday"):
        conn = http.client.HTTPSConnection("api.collectapi.com")
        headers = {
            'content-type': "application/json",
            'authorization': "apikey 4kgptyPM4eTgHnci9YAeH0:4n5gJ31Q1bj3VuInQiBmxB"
            }
        conn.request("GET", "/health/dutyPharmacy?ilce=Artuklu&il=Mardin", headers=headers)
        res = conn.getresponse()
        data = res.read()
        jsoneczane=data.decode("utf-8")
        eczaneler=json.loads(jsoneczane)["result"]
        baslik={"chat_id": f"{chat_id}","text":f"""
        Mardin Artuklu Nöbetçi Eczane
        """}
        requests.post(url,baslik).json()
        for eczane in eczaneler:
            telegram={"chat_id": f"{chat_id}","text":f""" 
{eczane["name"]} Eczanesi
Telefon Numarası= {eczane["phone"]}
Adres= {eczane["address"]}
Konum= https://maps.google.com/?q={eczane["loc"].split(",")[0]},{eczane["loc"].split(",")[1]}&ll={eczane["loc"].split(",")[0]},{eczane["loc"].split(",")[1]}&z=8
            """}
            requests.post(url,telegram).json()
        time.sleep(59)
    elif (str(turkeysaat2)=="08:01" or str(turkeysaat2)=="17:01") and (gun=="Saturday" or gun=="Sunday"):
        conn = http.client.HTTPSConnection("api.collectapi.com")
        headers = {
            'content-type': "application/json",
            'authorization': "apikey 4kgptyPM4eTgHnci9YAeH0:4n5gJ31Q1bj3VuInQiBmxB"
            }
        conn.request("GET", "/health/dutyPharmacy?ilce=Artuklu&il=Mardin", headers=headers)
        res = conn.getresponse()
        data = res.read()
        jsoneczane=data.decode("utf-8")
        eczaneler=json.loads(jsoneczane)["result"]
        baslik={"chat_id": f"{chat_id}","text":f"""
        Mardin Artuklu Nöbetçi Eczane
        """}
        requests.post(url,baslik).json()
        for eczane in eczaneler:

            telegram={"chat_id": f"{chat_id}","text":f""" 
{eczane["name"]} Eczanesi
Telefon Numarası= {eczane["phone"]}
Adres= {eczane["address"]}
Konum= https://maps.google.com/?q={eczane["loc"].split(",")[0]},{eczane["loc"].split(",")[1]}&ll={eczane["loc"].split(",")[0]},{eczane["loc"].split(",")[1]}&z=8
            """}
            requests.post(url,telegram).json()
        time.sleep(59)
    time.sleep(1)
