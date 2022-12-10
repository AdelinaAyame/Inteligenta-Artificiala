from urllib import request
import requests
API_KEY = "fb7a035d54daf544f2f708b83c60be43"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
 
city = input("Introduce numele Orasului: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(request_url)
 
if response.status_code == 200:
    data = response.json()
    vreme = data['weather'][0]['description']
    temperature = round(data["main"]["temp"],2)
    vant = round(data['wind']['speed'],2)
    print("Vremea: ", vreme)
    print("Temperatura", temperature)
    print("Vant", vant)
else:
    print("Am intampinat o eroare")