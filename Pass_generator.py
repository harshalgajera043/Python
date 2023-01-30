from tkinter import *
from tkinter import messagebox
import random
import pyperclip

PASSWORD_LENGTH = 12
BLUE = "#5BC0F8"
FONT = ("Arial", 10, "bold")
SMALL_ALPHA_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
CAP_ALPHA_LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
SPECIAL_CHAR_LIST = ["@", "_", "!", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?", "/", "!", "|", "}", "{", "~",
                     ":"]
NUMBER_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    pass_list = []
    # Special char
    for i in range(0, random.randint(1, 3)):
        pass_list.append(random.choice(SPECIAL_CHAR_LIST))

    # Numbers
    for j in range(0, random.randint(2, 4)):
        pass_list.append(str(random.choice(NUMBER_LIST)))

    # Caps
    for k in range(0, random.randint(2, 3)):
        pass_list.append(random.choice(CAP_ALPHA_LIST))

    for l in range(0, (PASSWORD_LENGTH-len(pass_list))):
        pass_list.append(random.choice(SMALL_ALPHA_LIST))

    random.shuffle(pass_list)
    # print(pass_list)

    update_password = "".join(pass_list)
    # for char in pass_list:
    #     update_password += str(char)
    print(update_password)

    # using pyperclip package for coping to the clipboard
    pyperclip.copy(update_password)

    password.delete(0, PASSWORD_LENGTH)
    password.insert(0, string=f"{update_password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def website():
    web = website_name.get()
    user = email.get()
    paskey = password.get()

    if web == "" or user == "" or paskey == "":
        if web == "":
            messagebox.showwarning(title="Warning", message="Website name is missing")
        elif user == "":
            messagebox.showwarning(title="Warning", message="User name is missing")
        else:
            messagebox.showwarning(title="Warning", message="Password is missing")
    else:
        popup = messagebox.askokcancel(title=web, message=f"These are the credential for {web} \nuser:{email.get()}"
                                                      f"\npaskey:{password.get()}\n Should you want to save it?")
        # print(popup)
        if popup:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{web} | {user} | {paskey}\n")

                entry_accepted_mess = messagebox.showinfo(title="New Entry Recorded", message=f"Successfully accepted {web}")

            website_name.delete(0, END)
            password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Generator")
window.minsize(width=450, height=280)
window.config(padx=50, pady=50)

# creating canvas to display logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.grid(column=1, row=0, columnspan=1)
My_pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=My_pass_img)


# creating labels of
title_label = Label(text="Website:", font=FONT)
title_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", font=FONT)
user_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)


# text_box to get user inputs
website_name = Entry(width=50)
website_name.grid(column=1, row=1, columnspan=2)
website_name.focus()


email = Entry(width=50)
email.insert(0, string="Harshalgajera65@gmail.com")
email.grid(column=1, row=2, columnspan=2)


password = Entry(width=33)  # justify=LEFT
password.grid(column=1, row=3)


space = Label().grid(column=0, row=4)


# let's create a generate password button
generate_password = Button(text="Generate Password", width=15, bg=BLUE, font=("Arial", 7, "bold"), command=password_generator).grid(column=2, row=3)

add_password = Button(text="Add", width=38, bg=BLUE, font=FONT, command=website).grid(column=1, row=5, columnspan=2)


window.mainloop()


