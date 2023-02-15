import requests

user_sheet_api = "https://api.sheety.co/7b478f6d9aaf388ebd365e03b4ec6f7e/flightDeals/users"

class UserInput():

    def take_input(self):
        first_name = input("What is your first name? ")
        last_name = input("Please enter your last name ")
        email = input("Enter your email here: ")

        post = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
        }}
        user_login = requests.post(url=user_sheet_api, json=post)
        print(user_login.json())

my_self = UserInput()
my_self.take_input()





