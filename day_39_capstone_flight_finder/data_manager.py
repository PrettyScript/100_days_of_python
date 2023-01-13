import config
import requests
from pprint import pprint

USERNAME = config.sheety_username
PROJECT_NAME = "flightDeals"
SHEET_NAME = "prices"

SHEETY_TOKEN = config.sheety_api_token
sheety_endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

sheety_headers = {
    "Authorization": SHEETY_TOKEN
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass
    
    def get_data(self):
        response = requests.get(url=sheety_endpoint, headers=sheety_headers)
        data = response.json()
        # print(response.text)
        pprint(data)