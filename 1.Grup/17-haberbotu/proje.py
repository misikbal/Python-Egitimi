import requests
import http.client
import time
import datetime
import pytz
import json
telegramUrl="https://api.telegram.org/bot5778559422:AAHtlHB-yssPkpNKkk4ynjWP6ThJOueqk_I/sendPhoto"

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 5YppkeyMa6sBAXPrgc97TU:74AWdsK0Mwi8OIW0UCnikO"
    }

conn.request("GET", "/news/getNews?country=tr&tag=technology", headers=headers)

res = conn.getresponse()
data = res.read()

haber=json.loads(data)
print(len(haber["result"]))
a=0
while a<len(haber["result"]):
    send={
        "chat_id":"967336300",
        "caption":f"""
{haber["result"][a]["name"]}

{haber["result"][a]["description"]}
<a href="{haber["result"][a]["url"]}">{haber["result"][a]["source"]} Sayfasına Git</a>
        """,
    "photo":f"""{haber["result"][a]["image"]}""",
    "parse_mode":"html"
    }
    requests.post(telegramUrl,send).json()
    a+=1