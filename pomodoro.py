from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
work_rep = 0
time_id = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global REPS
    global work_rep
    REPS = 0
    work_rep = 0
    timer_label.config(text="Timer", fg=GREEN)
    window.after_cancel(time_id)
    canvas.itemconfig(time, text="00:00")
    checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def on_start():
    global REPS
    global work_rep
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 2 != 0:
        timer(work_sec)
        timer_label.config(text="Let work Hard", fg=GREEN)
        work_rep += 1
        # checkmark.grid()
    elif REPS % 8 == 0:
        checkmark.config(text=work_rep * "✔")
        timer(long_break_sec)
        timer_label.config(text="Let's have some Netflix", fg=RED)
    else:
        checkmark.config(text=work_rep * "✔")
        timer(short_break_sec)
        timer_label.config(text="Have a break have a kit-kat", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def timer(count):
    global time_id
    min_remaining = count/60
    # print(min_remaining)
    sec_remaining = count % 60

    if sec_remaining < 10:
        sec_remaining = f"0{sec_remaining}"
    time_displayer = f"{int(count/60)}:{sec_remaining}"
    canvas.itemconfig(time, text=time_displayer)
    # print(count)
    if count > 0:
        time_id = window.after(1000, timer, count - 1)
    else:
        on_start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# window.minsize(width=600, height=450)
window.title("Podomoro Game GUI")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", font=(FONT_NAME, 28, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)
# timer_label.pack()


canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomoto_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomoto_img)
time = canvas.create_text(103, 137, text="00:00", font=(FONT_NAME, 24, "bold"), fill="white")
canvas.grid(column=1, row=1)
# canvas.pack()

# timer(5)

# Checkmark label
checkmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, "bold"))
# checkmark.config(pady=25, padx=10)
checkmark.grid(column=1, row=3)
# checkmark.pack()


# Create start and reset button
start_button = Button(text="Start", highlightthickness=0, command=on_start)
start_button.grid(column=0, row=2)
# start_button.place(x=-25, y=270)

restart_button = Button(text="Restart", highlightthickness=0, command=reset_timer)
restart_button.grid(column=2, row=2)
# restart_button.place(x=175, y=270)

window.mainloop()

