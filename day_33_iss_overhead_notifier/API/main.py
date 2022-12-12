import requests
from datetime import datetime

MY_LAT = 32.776665
MY_LONG = -96.796989
FORMATTED = 0

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

iss_data = iss_response.json()

longitude = float(iss_data["iss_position"]["longitude"])
latitude = float(iss_data["iss_position"]["latitude"])

iss_position = (longitude, latitude)
# print(iss_position)
my_position = (MY_LONG, MY_LAT)
# print(my_position)
parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": FORMATTED}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")

time_now = datetime.now()
print(f"Current time: {time_now.hour}")

# def is_sunset():
#     if sunset

# if iss_position == my_position and is_sunset:
#     print("send email")
# else:
#     print("Don't send email")
