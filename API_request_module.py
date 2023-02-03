import requests

iss_data = requests.get(url="http://api.open-notify.org/iss-now.json#")
# print(iss_data)
iss_data.raise_for_status()

data = iss_data.json()
current_position = data["iss_position"]
print(current_position)
