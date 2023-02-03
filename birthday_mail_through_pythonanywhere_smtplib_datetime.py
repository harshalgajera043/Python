import pandas
import datetime as dt
from random import *
import smtplib
from tkinter import messagebox

# -----------------------------  SENDING MECHANISM  -----------------------------#

def send_mail():
    send_me_to_your_friend = f"final_letter/letter_{randint(1, 3)}.txt"

    with open(send_me_to_your_friend) as letter:
        content = letter.read()
    # print(content)

    my_mail = "hgajera307@gmail.com"
    password = "zuxgytrgdqugfmmu"
    to_mail = f"{birthday_mail}"  # to avoid empty birthday_mail will add this piece of code into the function call
    # send_mail which we will call at PANDAS TO READ CSV section in last line after creating all the letters using
    # perpare letter function.

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs=to_mail, msg=f"Subject:Happy Birthday\n\n{content}")
        messagebox.showinfo(title=f"Birthday wish for {my_birthday}", message=f"Thanks for mailing")
        connection.quit()

#-----------------------------  LETTER CREATING MECHANISM  -----------------------------#


def prepare_letter():
    for i in range(1, 4):
        with open(f"letter_templates/letter_{i}.txt", "r") as letter:
            letter_list = letter.read()
            new_letter_1 = letter_list.replace("[NAME]", f"{my_birthday}")
            new_letter = new_letter_1.replace("Angela", "Harshal")
            with open(f"final_letter/letter_{i}.txt", "w") as letter_printed:
                letter_printed.write(new_letter)


#-----------------------------  DATETIME TO GET TODAY DATE  -----------------------------#

today = dt.datetime.now()
date = today.day
month = today.month
# print(today)

#-----------------------------  PANDAS TO READ CSV  -----------------------------#

wish_data = pandas.read_csv("data/data.csv")
wish_dict = wish_data.to_dict(orient="index")

global my_birthday
for i in range(0, len(wish_dict)):
    if date == wish_dict[i]["day"] and month == wish_dict[i]["month"]:
        print(wish_dict[i]["name"])
        birthday_mail = wish_dict[i]["email"]
        my_birthday = wish_dict[i]["name"]  # replace index with the index of birthday person
        prepare_letter()
        send_mail()
        # print(my_birthday)
