import config
import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API = config.tequila_api



class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        code = "TESTING"
        return code
        