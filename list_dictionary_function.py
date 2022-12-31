#Append for list and dictionary using functions
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, number_of_visit, Lst_of_place):
    dic_of_new_visit = {}
    dic_of_new_visit["country"] = country
    dic_of_new_visit["visits"] = number_of_visit
    dic_of_new_visit["cities"] = Lst_of_place
    travel_log.append(dic_of_new_visit)
    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
