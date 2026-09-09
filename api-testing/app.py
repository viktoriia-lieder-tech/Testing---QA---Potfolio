import requests
from pprint import pprint


url = "https://api.openweathermap.org/data/2.5/weather"

querystring = {"lat":"-33.87","lon":"151.21","appid":"96f41a956ced75bb226c6d9730d3d08c","lang":"de","units":"metric"}

payload = ""

response = requests.get(url, data=payload, params=querystring)

data = response.json()

print(response, type(response))

pprint(data)

#print(response.json())

#json

