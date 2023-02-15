import requests

sheety_endpoint = "https://api.sheety.co/7b478f6d9aaf388ebd365e03b4ec6f7e/userData/sheet1"

class User_login:

    # get to log-in
    def login(self, username, password):
        details = requests.get(url=sheety_endpoint)
        sheet_entries = details.json()["sheet1"]
        for i in range(0, len(sheet_entries)):
            if sheet_entries[i]["firstName"] == username and sheet_entries[i]["password"] == password:
                print("You have access")
            # else:
            #     print("Sorry no access")

    # put to change the password of already existing user
    def reset_password(self, username, password):
        details = requests.get(url=sheety_endpoint)
        sheet_entries = details.json()["sheet1"]
        quary = {"sheet1": {"password": password}}
        for i in range(0, len(sheet_entries)):
            put_url = f"{sheet_entries}/{sheet_entries[i]['id']}"
            if sheet_entries[i]["firstName"] == username:
                new_password_request = requests.put(url=put_url, data=quary)
                print(new_password_request.json())
                print("Password change Successfully")


    # post for new Sing up

    def create_account(self, details):
        new_account = requests.post(url=sheety_endpoint, json=details)
        print(new_account)


