import os
import requests
from twilio.rest import Client

account_sid = 'AC9bf00436b97ac2bfd0e0fba8f7a74d3b'
auth_token = os.environ.get("AUTH_TOKEN")

api_key= os.environ.get("API_KEY")
LAT = 42.360081
LNG = -71.058884

parameters ={
    "lat": LAT,
    "lon": LNG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url= "https://api.openweathermap.org/data/2.5/forecast?", params= parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
weather_list = weather_data["list"]
for hour_data in weather_list:
    condition_code = hour_data["weather"][0]['id']
    if  condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's going to rain today. Remember to bring an umbrella.",
        to='whatsapp:+18573761166'
    )

    print(message.status)



