#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import json
from pprint import pprint

Tequila_api_key = "cShzhQu2PchVn-qZ_f64hRbmxK06Tfvv"


sheety_api_key = "Bearer sasvjjJSvsb23d(23ds#@$asvbvds"
sheety_api_endpoint = "https://api.sheety.co/4e95935a5bd248856ece5911401d2537/flightDeals/prices"
sheety_put_api_endpoint = "https://api.sheety.co/4e95935a5bd248856ece5911401d2537/flightDeals/prices/2"


parameter = {
    "Authorization": sheety_api_key
}
# print(type(parameter))

add_city = {
    "price": {
        "city": "surat",
        "iatacode": "",
        "lowestPrice": 34
    }
}
# print(type(add_city))
#
# response = requests.get(url=sheety_api_endpoint, headers=parameter, json=add_city)
# # response = requests.post(url=sheety_api_endpoint, headers=parameter, json=add_city)
# pprint(response.json())

update_IATA = {"price": {
        "iatacode": "Training"
    }
}
#
response = requests.put(url=sheety_put_api_endpoint, headers=parameter, data=update_IATA)
print(response.json())



