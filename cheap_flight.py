from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

flight_details = DataManager()
flight_data = flight_details.sheet_data("mumbai", 54)

my_flight = FlightSearch()
# my_flight_code = my_flight.flight_code()
# print(my_flight_code)

update_IATA = flight_details.change_detail()
print(update_IATA)





# print("harshalTgajera".split("T"))
