import config
import requests

GENDER = "female"
WEIGHT = 65.78
HEIGHT = 157.48
AGE = 27

APP_ID = config.nutritionix_app_id
API_KEY = config.nutritionix_api_key
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

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
print(result)