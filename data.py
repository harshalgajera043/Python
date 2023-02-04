import requests

API_ENDPOINT = "https://opentdb.com/api.php?amount=10&type=boolean"

question_data = requests.get(API_ENDPOINT).json()["results"]
# print(question_data)
