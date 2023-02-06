import requests
import datetime as dt

PIXELA_TOKEN = "awddfghjwqrhacterge"
PIXELA_USERNAME = "harshal224"
PIXELA_API_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"


# Post to create or to post the graph on our request api endpoint after graph creation we have posted the event or activity on it.
# Put is used to modify predefine properties of our graphs

#---------------------------  POST  ---------------------------#

PIXELA_USER_PARAMS = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_API_ENDPOINT, json=PIXELA_USER_PARAMS)
# print(response.text)

GRAPH_API_ENDPOINT = "https://pixe.la/v1/users/harshal224/graphs"
GRAPH_CONFIG = {
    "id": GRAPH_ID,
    "name": "Coding Track",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

auth_config = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}
# response = requests.post(url=GRAPH_API_ENDPOINT, headers=auth_config, json=GRAPH_CONFIG)
# print(response.text)

today = str(dt.date.today().strftime('%Y%m%d'))
print(today)

post_endpoint = f"{PIXELA_API_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"

post_params = {
    "date": today,
    "quantity": "9",
}

# response = requests.post(url=post_endpoint, headers=auth_config, json=post_params)
# print(response.text)


#---------------------------  PUT_ENTRIE_API  ---------------------------#

put_config = {
    "color": "kuro"
}
#
# put_response = requests.put(url=post_endpoint, headers=auth_config, json=put_config)
# print(put_response.text)

#-------------------  PUT PIXEL  -------------------#

put_config_pixel = {
    "quantity": "1"
}

put_endpoint = f"{PIXELA_API_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{today}"
put_response = requests.put(url=put_endpoint, headers=auth_config, json=put_config_pixel)

print(put_response.text)
#-------------------------  DELETE  -------------------------#
#
# delete_endpoint = f"{post_endpoint}/{today}"
#
# delete_response = requests.delete(url=delete_endpoint, headers=auth_config)
# print(delete_response.text)



