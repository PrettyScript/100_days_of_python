import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 32.776665
MY_LONG = -96.796989
FORMATTED = 0

MY_EMAIL = "jessicatestingwithpython@gmail.com"
MY_PASSWORD = "iwuxecmvqpbgznas"

def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_data = iss_response.json()

    longitude = float(iss_data["iss_position"]["longitude"])
    latitude = float(iss_data["iss_position"]["latitude"])

    iss_position = (longitude, latitude)
    my_position = (MY_LONG, MY_LAT)

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": FORMATTED}

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(data)
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")

    time_now = datetime.now().hour()
    # print(f"Current time: {time_now.hour}")

    if time_now >= sunset or time_now <= sunrise:
        return True

# def is_sunset():
#     if sunset

# if iss_position == my_position and is_sunset:
#     print("send email")
# else:
#     print("Don't send email")

while True:
    time.sleep(60)
    if is_iss_overhead and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Look Up\n\nThe ISS is above you in the sky.")
