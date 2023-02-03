import requests
import datetime as dt
from smtplib import *

MY_EMAIL = "hgajera307@gmail.com"
PASSWORD = "tgxvkoydlyledscg"
My_lat = 23.0300
My_long = 72.5800

PARAMETERS = {
    "lat": My_lat,
    "lng": My_long,
}

#--------------------------------  MAIL SENDING MECHANISM USING SMTP  --------------------------------#

def send_mail():
    connection = SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Internation Space Station Notification"
                                                                   "\n\nInternation space station is visible from"
                                                                   " the ground.")
    connection.close()


#--------------------------------  CURRENT TIME ON THE BASIS OF CURRENT LOCATION  --------------------------------#


sun_time = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={My_lat}&lng={My_long}&formatted=0")
sun_time.raise_for_status()
data = sun_time.json()
# print(data)

sunrise_time = data["results"]["sunrise"]
sunrise_time_list_1 = sunrise_time.split("T")
sunrise_hour_int = int(sunrise_time_list_1[1].split(":")[0])
# print(sunrise_hour_int)


sunset_time = data["results"]["sunset"]
sunset_time_list_1 = sunset_time.split("T")
sunset_hour_int = int(sunset_time_list_1[1].split(":")[0])
# print(sunset_hour_int)

today = dt.datetime.now()
today_time = today.time()
current_hour = today_time.hour
# print(current_hour)


#---------------  MECHANISM TO COMPARE OUR CURRENT POSITION AND ISS's  POSITION  ---------------#

iss_position = requests.get("http://api.open-notify.org/iss-now.json")
iss_pos_data = iss_position.json()
# print(iss_pos_data)
iss_long = iss_pos_data["iss_position"]["longitude"]
iss_lan = iss_pos_data["iss_position"]["latitude"]
# print(iss_lan)
# print(iss_long)

# will send the mail to user only in the condition that time is in between sunset and sunrise hour and ISS is excatly
# over the head of person on the basis of his live location which we get as an input

if current_hour <= sunrise_hour_int or current_hour >= sunset_hour_int:
    if iss_long == My_long and iss_lan == My_lat:
        send_mail()
