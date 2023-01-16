import requests
from pprint import pprint


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, flight_data):
        self.flights = flight_data

    def get_IATA_code(self):
        # pprint(self.flights)
        flights = self.flights
        print(flights[0]["iataCode"])
        for flight in flights:
            # print(flight["iataCode"])
            try:
                flight["iataCode"] = ""
            except KeyError:
                flight["iataCode"] = ""
                
            if flight["iataCode"] == "":
                # flight["iataCode"] = 'TESTING'
                print("True")
                
        print(flights)
                
                
    #     try:
    #         numbers[key] += 1
    #     except KeyError:
    #         numbers[key] = 1
        
