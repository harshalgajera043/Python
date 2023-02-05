import requests
from smtplib import *
import os
from twilio.rest import Client

# TWILIO_SID = "AC42ffd62c484718ff17bccdb893f6e71e"
# TWILIO_PASSWORD = "3bc3c9367885423f55ec796b2db3c644"
#
# client = Client(TWILIO_SID, TWILIO_PASSWORD)
#
# message = client.messages \
#                 .create(
#                      body="Bring an Umbrella",
#                      from_='+15017122661',
#                      to='+15558675310'
# )

API_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"
PARAMETERS = {
    "lat": -19.760250,
    "lon": -42.076580,
    "id": 524901,
    "exclude": "city",
    "appid": "2b471c9b4bc9cb14e3df03b0b9498190",
}

from_id = "Hgajera307@gmail.com"
to_id = "Hgajera307@gmail.com"
password = "fysyoaxiwlscgbzg"


response = requests.get(API_ENDPOINT, params=PARAMETERS)
weather_data = response.json()

weather_data_list = weather_data["list"][:12]  # list index for weather data
# print(weather_data_list)

rain_day = [weather_condition["weather"][0]["id"] for weather_condition in weather_data_list if weather_condition["weather"][0]["id"] < 700]
if len(rain_day) > 0:
    connection = SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=from_id, password=password)
    connection.sendmail(from_addr=from_id, to_addrs=to_id, msg=f"Subject: Weather Updates\n\nIt will goin to be a rainy day. Remember to bring an Umbrella")

# need_for_umbrella = []
# for i in range(0, 12):
#     weather_condition_id = weather_data_list[i]["weather"][0]["id"]
#     if weather_condition_id < 800:
#         need_for_umbrella.append(i)
# if len(need_for_umbrella) > 0:
#     print("Bring an umbrella")
# else:
#     print("No need to take umbrella")




