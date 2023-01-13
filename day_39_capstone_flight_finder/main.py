# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data = DataManager()

sheet_data = data.get_data()
# pprint(sheet_data)

test_city = sheet_data[0]

flight_search = FlightSearch(test_city)
flight_search.get_IATA_code(test_city)
