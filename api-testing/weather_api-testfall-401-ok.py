#
#Testfall 02
#Anforderug: Gültige Stadt + ungültiger API-Key
#Erwartung: 401 OK


import requests

import os
from dotenv import load_dotenv
load_dotenv()

ungültiger_api_key = os.getenv("UNGÜLTIGER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def test_current_wheather_401():
    params = {
        "q": "Leipzig, DE",
        "appid": ungültiger_api_key,
        "lang": "de",
        "units": "metric"
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10
    )

    body = response.json()

    print("\nTestfall 02 - Response:")
    print(body)

    assert response.status_code == 401
    assert "message" in body
    assert int(body["cod"]) == 401
    