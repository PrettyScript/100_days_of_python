import config
import requests
from pprint import pprint


USERNAME = config.sheety_username
PROJECT_NAME = "flightDeals"
SHEET_NAME = "prices"

SHEETY_TOKEN = config.sheety_api_token
sheety_endpoint = (
    f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
)

sheety_headers = {"Authorization": SHEETY_TOKEN}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        
    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data)
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "prices": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)
