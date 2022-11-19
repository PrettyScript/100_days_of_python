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
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)
# # avg_temp = sum(temp_list) / len(temp_list)
# # print(f"Average temp: {round(avg_temp)}")

# print(data['temp'].mean())
# print(data['temp'].max())

# # Get Data in Columns
# print(data['condition'])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
# print(monday.condition)

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(celsius_to_fahrenheit(monday.temp))

# Create a dataframe from scratch
student_scores = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(student_scores)
# print(data)
data.to_csv("new_data.csv")