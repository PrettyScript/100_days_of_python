import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city = city

    def get_IATA_code(self, city):
        print(city)
