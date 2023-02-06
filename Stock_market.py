import datetime as dt
import os
import requests
from smtplib import *

#-------------------  DATETIME MODULE TO GET PRESENT DAY  -------------------#

# today = dt.date.today()
today = dt.date(year=2023, month=2, day=4)
yesterday = today - dt.timedelta(days=1)
yesterday_before = today - dt.timedelta(days=2)
past_two_days = [yesterday.isoformat(), yesterday_before.isoformat()]

#---------------------------  API - IMPORT DATA USING API KEY  --------------------------#

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# AVS_API_KEY = os.environ.get("API_KEY")
AVS_API_KEY = "K6JFQGSQL3Z7M2D4"
AVS_API_ENDPOINT = "https://www.alphavantage.co/query"

PARAMETERS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": AVS_API_KEY,
}

# Requesting API provider to share the daily data to access the closing stock price of for last two days
stock_data = requests.get(url=AVS_API_ENDPOINT, params=PARAMETERS)
stock_data = stock_data.json()["Time Series (Daily)"]

past_two_closed = [float(stock_data[date]["4. close"]) for date in past_two_days]

daily_change = past_two_closed[0] - past_two_closed[1]
daily_change_percentage = round(daily_change*100/past_two_closed[0], 2)

if daily_change_percentage >= 0.8 or daily_change_percentage <= -5:

    # -----------------------  API TO CREATE NEWS  -----------------------#

    NEWS_API_KEY = "46f2a5942f5f492cb56b1e46bb1f99f7"
    NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

    NEWS_PARAMETERS = {
        "q": COMPANY_NAME,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
        "language": "en"
    }

    news = requests.get(url=NEWS_API_ENDPOINT, params=NEWS_PARAMETERS)
    news_details = news.json()["articles"][:3]
    news_list_headlines = [detail["title"] for detail in news_details]
    news_list_description = [detail["description"] for detail in news_details]

    if daily_change_percentage > 0.5:
        msg = f"TSLA 2%\nHeadline: {news_list_headlines[0]}\nBrief: {news_list_description[0]}"
        # \nor\nHeadline: {news_list_headlines[1]}\nBrief: {news_list_description[1]}\nor\nHeadline: {news_list_headlines[2]}\nBrief: {news_list_description[2]}
        print(msg)
    else:
        msg = f"TSLA 5%\nHeadline: {news_list_headlines[0]}\nBrief: {news_list_description[0]}"
        # \nor\nHeadline: {news_list_headlines[1]}\nBrief: {news_list_description[1]}\nor\nHeadline: {news_list_headlines[2]}\nBrief: {news_list_description[2]}"

    # ------------------------  SMTP TO SEND THE MAIL RELATED TO CHANGE  ------------------------#
    from_id = "hgajera307@gmail.com"
    receive_id = "hgajera65@gmail.com"
    password = "znxbjxstkvuwkizz"

    send_mail = SMTP("smtp.gmail.com", 587)
    send_mail.starttls()
    send_mail.login(user=from_id, password=password)
    send_mail.sendmail(from_addr=from_id, to_addrs=receive_id, msg=f"Subject:Market Updates\n\n{msg}")

