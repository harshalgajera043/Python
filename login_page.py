from tkinter import *
from sheety import User_login
import requests

BG_COLOR = "#D1FFF3"
sheety_endpoint = "https://api.sheety.co/7b478f6d9aaf388ebd365e03b4ec6f7e/userData/sheet1"

user = User_login()

def user_name():
    username_label.config(text="Username/Email:")
    sign_in_button.grid(column=1, row=3, pady=10)
    forget_pass_button.grid(column=2, row=3, pady=10)
    password_label.config(text="Password:")
    forget_pass_button.config(text="Forget Password")
    if firstname.get() != "" and password.get() != "":
        user.login(firstname.get(), password.get())
        firstname.delete(0, END)
        password.delete(0, END)


def forget_password():
    # username_label.config(text="New Password:")
    forget_pass_button.grid(column=2, row=3, pady=10)
    sign_in_button.grid_forget()
    password_label.config(text="New Password:")
    forget_pass_button.config(text="Save Password")
    if firstname.get() != "" and password.get() != "":
        name = firstname.get()
        quary = {"sheet1": {"password": password.get()}}
        details = requests.get(url=sheety_endpoint)
        sheet_entries = details.json()["sheet1"]
        for i in range(0, len(sheet_entries)):
            id = sheet_entries[i]['id']
            if sheet_entries[i]["firstName"] == name:
                put_url = f"{sheety_endpoint}/{id}"
                change_password = requests.put(url=put_url, json=quary)
                print(change_password.json())
        sign_in_button.grid(column=1, row=3, pady=10)
        print("Successfully saved your new password")
        firstname.delete(0, END)
        password.delete(0, END)
        user_name()
    # If both the entry matches update(put) this new password in sheet password row for the user
    """Check for the username in sheet if their then compare both the passwords if matches then user message box to 
    display you have access else warning that username or password entered is not matching"""

def new_account():
    sign_in_button.grid_forget()
    forget_pass_button.grid_forget()
    new_account_button.grid_forget()
    new_account_button.config(text="Create Account")

    firstname_label.grid(column=0, row=0, pady=5)
    # will replace username label with Last name to reduce the griding
    username_label.config(text="Last Name:")

    # And password with email
    password_label.config(text="Email Id:")

    new_account_pass_label.grid(column=0, row=3, pady=5)

    new_account_button.grid(column=0, row=4, columnspan=3)
    firstname.grid(column=1, row=0, columnspan=2, pady=5)
    # firstname.focus()
    lastname.grid(column=1, row=1, columnspan=2, pady=5)
    email.grid(column=1, row=2, columnspan=2, pady=5)
    password.grid(column=1, row=3, columnspan=2, pady=5)

    user_info = {"sheet1": {
        "firstName": f"{firstname.get()}",
        "lastName": f"{lastname.get()}",
        "eMail": f"{email.get()}",
        "password": f"{password.get()}",
    }}

    if firstname.get() != "" and lastname.get() != "" and email.get() != "" and password.get() != "":
        user.create_account(user_info)
        print(user_info)

        firstname.delete(0, END)
        lastname.delete(0, END)
        email.delete(0, END)
        password.delete(0, END)

        new_account_button.grid_forget()
        firstname_label.grid_forget()
        new_account_pass_label.grid_forget()
        firstname.grid_forget()
        password.grid_forget()





        user_name()






# Main code
window = Tk()
window.title("Login")
window.config(height=400, width=350, bg=BG_COLOR, pady=30, padx=30)

# Labels
firstname_label = Label(text="First Name:", bg=BG_COLOR)

username_label = Label(text="Username/Email:", bg=BG_COLOR)
username_label.grid(column=0, row=1, pady=5)

password_label = Label(text="Password:", bg=BG_COLOR)
password_label.grid(column=0, row=2, pady=5)

new_account_pass_label = Label(text="Password:", bg=BG_COLOR)

# User inputs
firstname = Entry(width=32)
firstname.focus()
firstname.grid(column=1, row=1, columnspan=2, pady=5)

lastname = Entry(width=32)

email = Entry(width=32)

# password
password = Entry(width=32)
password.grid(column=1, row=2, columnspan=2, pady=5)

# Login button
sign_in_button = Button(text="Sing In")
sign_in_button.config(command=user_name)
sign_in_button.grid(column=1, row=3)

# Create new account button
new_account_button = Button(text="New Account")
new_account_button.config(command=new_account)
new_account_button.grid(column=0, row=3)

forget_pass_button = Button(text="Forget Password?")
forget_pass_button.config(bg=BG_COLOR, highlightthickness=0, command=forget_password)
forget_pass_button.grid(column=2, row=3, pady=10)

window.mainloop()
