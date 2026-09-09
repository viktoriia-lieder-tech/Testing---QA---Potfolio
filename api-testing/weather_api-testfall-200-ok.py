#
#Testfall 01
#Anforderug: Gültige Stadt + gültiger API-Key
#Erwartung: 200 OK


import requests

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv.("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def test_current_wheather_200():
    params = {
        "q": "Leipzig, DE",
        "appid": api_key,
        "lang": "de",
        "units": "metric"
    }

    response = requests.get(
        BASE_URL,
        params = params,
        timeout = 10
    )

    body = response.json()

    print("\nTestfall 01 - Response:")
    print(body)

    assert response.status_code == 200
    assert body["name"] == "Leipzig"
    assert "weather" in body
    assert isinstance(body["whather"], list)
    assert len(body["weather"]) > 0
    assert "main" in body
    assert "temp" in body["main"]
    assert int(body["cod"]) == 200
    