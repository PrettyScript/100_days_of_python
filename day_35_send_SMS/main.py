import requests
import os
from twilio.rest import Client
import config



# Dallas
LAT = "32.776665"
LON = "-96.796989"

# Los Angeles 
# LAT = "34.052235"
# LON = "-118.243683"

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = config.OWM_api_key
account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token

weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()

# weather_data = response.json()["hourly"][0]["weather"][0]["id"]
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                body="It's going to rain today. Remember to bring an ☔️.",
                                from_=config.twilio_phone_num,
                                to=config.my_phone_num
                            )
    

    print(message.status)