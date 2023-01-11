import requests
from datetime import datetime
import config

USERNAME ="prettyscript"
TOKEN = config.pixela_user_token
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now().strftime("%Y%m%d")

post_habit_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
post_to_graph_params = {
    "date": today,
    "quantity": input("How many hours did you code today? ")
}

# response = requests.post(url=post_habit_endpoint, json=post_to_graph_params, headers=headers)
# print(response.text)

update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
update_graph_params = {
    "quantity": "320"
}

# response = requests.put(url=update_graph_endpoint, json=update_graph_params, headers=headers)
# print(response.text)

delete_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230110"

response = requests.delete(url=delete_graph_endpoint, headers=headers)
print(response.text)


