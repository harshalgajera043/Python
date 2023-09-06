from geopy.geocoders import Nominatim
import geopy.distance
import math

OPERATION_PLACE = ["Phoenix", "Dallas", "Houston", "Las Vegas", "Nashville", "New York City", "New Orleans", "San Francisco", "Seattle", "Austin", "Chicago", "San Diego"]
INVENTORY_LOCATION = {}

#------------------------------- LOCATION COLLECTOR --------------------#
# This function will return the latitude and longitude based on the city_name enterd
# Will be using this function to get the idea about our inventory location as well as the location of delivery
# after tgetting the inital location of user and inverntory we will indenify the nearest invenrtory location using for loop in combination with if condition and distance function
def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_coordinates")
    location = geolocator.geocode(city_name, exactly_one=True)

    if location:
        return location.latitude, location.longitude
    else:
        return None

# print(type(get_coordinates("tempe")))


# Using for loop for getting the location our Inventory
for city in OPERATION_PLACE:
    city_location = get_coordinates(city)
    INVENTORY_LOCATION[city] = city_location
# print(INVENTORY_LOCATION)

# --------------------------- DISTANCE CALCULATOR -------------------------#
def distance_calculator(inventory_city, user_city):
    distance = (geopy.distance.geodesic(inventory_city, user_city).miles)
    return distance

#----------------------- USER DETAILS COLLECTION -----------------------#
user_city = input("Enter you city of leaving\n").capitalize()

user_lat_log_location = get_coordinates(user_city)
# print(user_lat_log_location)

#---------------------- INVENTORY SUGGESTION ----------------------------#

distance_dict = {}
for city in OPERATION_PLACE:
    operation_axis = INVENTORY_LOCATION[city]
    distance = round(distance_calculator(operation_axis, user_lat_log_location), 2)
    distance_dict[city] = distance
# print(distance_dict)

smallest_distance = 0
distance_list = []
# for city in distance_dict:
#     if smallest_distance == 0:
#         smallest_distance = distance_dict[city]
#     elif smallest_distance > distance_dict[city]:
#         smallest_distance = distance_dict[city]

for city in distance_dict:
    distance_list.append(distance_dict[city])
smallest_distance = min(distance_list)

nearest_inventory_location = list(distance_dict.keys())[list(distance_dict.values()).index(smallest_distance)]

print(f"Your nearest inventory location is {nearest_inventory_location}")
