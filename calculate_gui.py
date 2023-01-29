from tkinter import *

window = Tk()
window.minsize(width=150, height=200)
window.title("Calculator")
# window.config(pady=10, padx=10)

# key_location = [(1, 4), (0, 3), (1, 3), (2, 3), (0, 2), (1, 2), (2, 2), (0, 1), (1, 1), (2, 1)]


def display_entry_0():
    return 0


def display_entry_1():
    return 1


def display_entry_2():
    return 2


def display_entry_3():
    return 3


def display_entry_4():
    return 4


def display_entry_5():
    return 5


def display_entry_6():
    return 6


def display_entry_7():
    return 7


def display_entry_8():
    return 8


def display_entry_9():
    return 9


def display_entry_equal():
    return "="


def display_entry_devide():
    return "/"


def display_entry_multiply():
    return "*"


def display_entry_substract():
    return "-"


def display_entry_add():
    return "+"


# Button name 0
button_0 = Button(text=0, command=str(display_entry_0))
button_0.grid(column=1, row=4)

# Button name 1
button_1 = Button(text=1, command=str(display_entry_1))
button_1.grid(column=0, row=3)

# Button name 2
button_2 = Button(text=2, command=str(display_entry_2))
button_2.grid(column=1, row=3)

# Button name 3
button_3 = Button(text=3, command=str(display_entry_3))
button_3.grid(column=2, row=3)

# Button name 4
button_4 = Button(text=4, command=str(display_entry_4))
button_4.grid(column=0, row=2)

# Button name 5
button_5 = Button(text=5, command=str(display_entry_5))
button_5.grid(column=1, row=2)

# Button name 6
button_6 = Button(text=6, command=str(display_entry_6))
button_6.grid(column=2, row=2)

# Button name 7
button_7 = Button(text=7, command=str(display_entry_7))
button_7.grid(column=0, row=1)

# Button name 8
button_8 = Button(text=8, command=str(display_entry_8))
button_8.grid(column=1, row=1)

# Button name 9
button_9 = Button(text=9, command=str(display_entry_9))
button_9.grid(column=2, row=1)

# Button name =
button_equal = Button(text="=", command=str(display_entry_equal))
button_equal.grid(column=3, row=0)

# Button name /
button_devide = Button(text="/",command=str(display_entry_devide))
button_devide.grid(column=3, row=1)

# Button name *
button_multiply = Button(text="*", command=str(display_entry_multiply))
button_multiply.grid(column=3, row=2)

# Button name -
button_substract = Button(text="-", command=str(display_entry_substract))
button_substract.grid(column=3, row=3)

# Button name +
button_add = Button(text="+", command=str(display_entry_add))
button_add.grid(column=3, row=4)








# screen = Label(text=0)
# screen.place(x=0, y=0)
# screen.config(width=7)

# operations =


window.mainloop()
