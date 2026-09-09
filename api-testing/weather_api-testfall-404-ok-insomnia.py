#
#Testfall 03
#Anforderug: Ungültige Stadt + gültiger API-Key
#Erwartung: 404 OK

import requests
from pprint import pprint

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

url = "https://api.openweathermap.org/data/2.5/weather"

#def test_current_wheather_404():
#    params = {
#        "q": "XyzTestCity987654321",
#        "appid": api_key,
#        "lang": "de",
#        "units": "metric"
#    }

#    response = requests.get(
#        url,
#        params=params,
#        timeout=10
#    )

querystring = {"q":"XyzTestCity987654321","appid":api_key,"lang":"de","units":"metric"}

payload = ""

response = requests.get(url, data=payload, params=querystring)

data = response.json()

print(response, type(response))

pprint(data)

