import config
import requests


TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_API = config.tequila_api
headers = {
    "apikey": TEQUILA_API
}

class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self) -> None:
        pass
    def get_flight_price(self, destination_city):
        params = {
          "fly_from": "DFW",
          "fly_to" : destination_city,
          "date_from": "01/24/2023",
          "date_to": "07/24/2023",
          "nights_in_dst_from": 7,
          "nights_in_dst_to": 28,
          "flight_type": "round",
          "one_for_city": 1,
          "max_stopovers": 0,
          "curr": "USD",
          "max_stopovers": 0
        }
        response = requests.get(url=TEQUILA_ENDPOINT, headers=headers, params=params)
        response.raise_for_status()
        print(response.json())
        
    # get_flight_price("SEA")