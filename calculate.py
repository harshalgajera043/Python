from tkinter import *

window = Tk()
window.title("Calculator")
window.minsize(width=150, height=200)


def perform():
    display_score = Label(text="0", font=("Arial", 54, "bold"))
    display_score.clipboard_clear()
    display_score.grid(column=1, row=8)
    num_1 = float(input_1.get())
    num_2 = float(input_2.get())
    result = 0
    if radio_state.get() == 1:
        result = num_1 + num_2
    elif radio_state.get() == 2:
        result = num_1 - num_2
    elif radio_state.get() == 3:
        result = num_1 * num_2
    elif radio_state.get() == 4:
        result = num_1 / num_2
    display_score.config(text=f"{round(result, 2)}")


# 1st input
input_1 = Entry()
input_1.insert(index=0, string=0)
input_1.grid(column=0, row=0)
input_1.focus()


# operation
def radio_user():
    print(radio_state.get())


radio_state = IntVar()
radio_add = Radiobutton(text="+", value=1, variable=radio_state, command=radio_user)
radio_add.grid(column=1, row=0)

radio_sub = Radiobutton(text="-", value=2, variable=radio_state, command=radio_user)
radio_sub.grid(column=1, row=1)

radio_multi = Radiobutton(text="*", value=3, variable=radio_state, command=radio_user)
radio_multi.grid(column=1, row=2)

radio_devide = Radiobutton(text="/", value=4, variable=radio_state, command=radio_user)
radio_devide.grid(column=1, row=3)

# 2nd input
input_2 = Entry()
input_2.insert(index=0, string=0)
input_2.grid(column=2, row=0)

calculate = Button(text="Calculate")
calculate.grid(column=1, row=5)
calculate.config(command=perform)





window.mainloop()
