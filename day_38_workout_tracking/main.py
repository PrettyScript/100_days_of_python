import config
import requests
from datetime import datetime

GENDER = "female"
WEIGHT = 65.78
HEIGHT = 157.48
AGE = 27

USERNAME = config.sheety_username
PROJECT_NAME = "myWorkouts"
SHEET_NAME = "workouts"
TOKEN = config.sheety_token

APP_ID = config.nutritionix_app_id
API_KEY = config.nutritionix_api_key
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

user_response = input("Tell me which exercise you did: ")

exercise_params = {
    "query":user_response,
    "gender":GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()

sheety_headers = {
    "Authorization": TOKEN
}

now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%I:%M:%S")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout" : {
            "date":date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }        
    }



    add_row_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_headers)
    add_row_response.raise_for_status()
    print(add_row_response.text)
