# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data = DataManager()
sheet_data = data.get_destination_data()
pprint(sheet_data)


