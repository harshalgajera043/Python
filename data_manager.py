import requests
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint

class DataManager:

    def __init__(self):
        self.my_flight = FlightSearch()
        self.cheap_flight = FlightData()
        self.Tequila_api_key = "cShzhQu2PchVn-qZ_f64hRbmxK06Tfvv"
        self.sheety_api_key = "Bearer asfojJihNF874&HJ@xwji2vasc214*&23"
        self.sheety_api_endpoint = "https://api.sheety.co/da01725c6ec4a96c30c5a6da1f0f92f7/flightDeals/prices"
        self.parameter = {
            "Authorization": self.sheety_api_key
        }

    def sheet_data(self, city_name, lower_price):

        self.add_city = {
            "price": {
                "city": f"{city_name}",
                "iataCode": "",
                "lowestPrice": lower_price
            }
        }

        # self.post_city = requests.post(url=self.sheety_api_endpoint, headers=self.parameter, json=self.add_city).json()
        self.response = requests.get(url=self.sheety_api_endpoint, headers=self.parameter, json=self.add_city).json()
        print(self.response)
        self.city = self.response["prices"]
        return self.response

    def change_detail(self):
        for i in range(len(self.city)):
            self.flight_code = self.my_flight.flight_code(self.city[i]["city"])
            self.lowest_price = self.city[i]["lowestPrice"]
            update = {
                "price": {
                    "iataCode": f"{self.flight_code}"
                }
            }
            # print(i)
            if self.city[i]["iataCode"] == "":
                self.id = self.city[i]["id"]
                self.sheeety_put_api = f"{self.sheety_api_endpoint}/{self.id}"
                print(self.response["prices"][i]["id"])
                self.updated_response = requests.put(url=self.sheeety_put_api, headers=self.parameter, json=update)
            self.look_for_trip(self.flight_code, self.lowest_price)
        self.final_response = requests.get(url=self.sheety_api_endpoint, headers=self.parameter, json=self.add_city).json()
        # print(self.final_response)
        return self.final_response


    def look_for_trip(self, flight_code, lowest_price):
        self.cheap_flight.trip(flight_code, lowest_price)


