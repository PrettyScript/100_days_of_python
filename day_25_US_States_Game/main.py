# with open("weather_data.csv") as data:
#     weather_data = data.readlines()
#     print(weather_data)
    
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperatures = []
#     for row in data:

#         temperature = row[1]
#         if temperature != 'temp':
#             temperatures.append(int(temperature))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
# print(data["temp"])
