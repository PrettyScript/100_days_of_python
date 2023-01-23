import config
import requests
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_API = config.tequila_api




class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport"
        }
        headers = {
            "apikey": TEQUILA_API
        }
        response = requests.get(url=TEQUILA_ENDPOINT, params=params, headers=headers)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code
