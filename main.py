import requests
from datetime import *

USERNAME = "zaeff"
TOKEN = "sldkgfjhsdghdkl909augk"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
ID = "graph1"

user_parametrs = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_parameters = {
    "id": ID,
    "name": "Swimming graph",
    "unit": "meter",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# respond = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(respond.text)

pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}"

#
# pixel_parameters = {
#     "date": "20230101",
#     "quantity": "500",
#     "optionalData": '{"circuit number": 10, "circuit length": 25}'
# }
#
# respond = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
# print(respond.text)
day = datetime(year=2023, month=1, day=1)

pixel_put_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}/{day.strftime('%Y%m%d')}"

pixel_parameters = {
    "quantity": "1500",
}

# respond = requests.put(url=pixel_put_endpoint, json=pixel_parameters, headers=headers)
# print(respond.text)

respond = requests.delete(url=pixel_put_endpoint, headers=headers)
print(respond.text)

