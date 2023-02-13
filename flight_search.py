import requests
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "cShzhQu2PchVn-qZ_f64hRbmxK06Tfvv"

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.key_header = {"apikey": TEQUILA_API_KEY}
        self.location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

    def flight_code(self, city_name):
        self.query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=self.location_endpoint, headers=self.key_header, params=self.query)
        self.code = response.json()["locations"][0]["code"]
        print(self.code)
        return self.code

