from tkinter import *
import random
import pandas

LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"


# Import word list here which helps us make random word choice
word_file = "../day_31/data/french_words.csv"
data_file = pandas.read_csv(word_file)

# Making the list of word from csv to access and making random choice
french_word_list = [word for word in data_file["French"]]
# print(french_word_list)

current_word = random.choice(french_word_list)
# answer_word = data_file[data_file["French"] == current_word]["English"].item()
# print(answer_word)


#----------------------------  FUNCTIONS  ----------------------------#


# display card_back
def card_back_side():
    answer_word = data_file[data_file["French"] == current_word]["English"].item()
    # card_back = PhotoImage(file="../day_31/image/card_back.png")
    canvas.create_image(400, 267, image=CARD_BACK)
    canvas.create_text(400, 150, text="English", fill="white", font=LANGUAGE_FONT)
    canvas.create_text(400, 267, text=f"{answer_word}", fill="white", font=WORD_FONT)


# Display card_front
def canvas_front():
    global current_word
    global CARD_FRONT
    current_word = random.choice(french_word_list)
    # front_card = PhotoImage(file="../day_31/image/card_front.png")
    canvas.create_image(400, 267, image=CARD_FRONT)
    canvas.create_text(400, 150, text="French", fill="black", font=LANGUAGE_FONT)
    canvas.create_text(400, 267, text=f"{current_word}", fill="black", font=WORD_FONT)
    canvas.after(3000, card_back_side)


def known():
    # canvas.after_cancel(first)
    global french_word_list
    french_word_list.remove(current_word)
    canvas_front()
    # print(len(french_word_list))
    # print("You know me")


def unknown():
    canvas_front()


#---------------------------------  UI DESIGN  ---------------------------------#
# Create a window to display

window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

CARD_FRONT = PhotoImage(file="../day_31/image/card_front.png")
CARD_BACK = PhotoImage(file="../day_31/image/card_back.png")

# Create a canvas using Canvas class from tkinter
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# card_front = PhotoImage(file="../day_31/image/card_front.png")
background = canvas.create_image(400, 267, image=CARD_FRONT)
language_text = canvas.create_text(400, 150, text="French", fill="black", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 267, text=f"{current_word}", fill="black", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

first = canvas.after(3000, card_back_side)

# Let's create two button wrong and right
right_image = PhotoImage(file="../day_31/image/right.png")
right = Button(image=right_image, highlightthickness=0, command=known)
right.grid(column=1, row=1)

wrong_image = PhotoImage(file="../day_31/image/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=unknown)
wrong.grid(column=0, row=1)

window.mainloop()
