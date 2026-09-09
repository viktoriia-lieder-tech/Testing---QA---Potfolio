#
#Testfall 03
#Anforderug: Ungültige Stadt + gültiger API-Key
#Erwartung: 404 OK

import requests

import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def test_current_wheather_404():
    params = {
        "q": "XyzTestCity987654321",
        "appid": api_key,
        "lang": "de",
        "units": "metric"
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10
    )

    body = response.json()

    print("\nTestfall 03 - Response:")
    print(body)

    assert response.status_code == 404
    assert "message" in body
    assert int(body["cod"]) == 404
    