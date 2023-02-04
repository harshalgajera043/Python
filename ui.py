from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text='question',
                                                     justify="center",
                                                     fill=THEME_COLOR,
                                                     width=250,
                                                     font=("Arial", 20, "italic")
                                                     )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Create Button
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        # True button
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        # False Button
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        # Score Label
        self.scoreboard = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR, font=("Arial", 14, "bold"))
        self.scoreboard.grid(column=1, row=0)

        # question
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You reach the quiz end")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def reset(self):
        self.canvas.config(bg="white")

    def true_pressed(self):
        user_answer = "True"
        answer = self.quiz.check_answer(user_answer)
        self.scoreboard.config(text=f"Score: {self.quiz.score}")

        if answer == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.reset)

        self.get_next_question()


    def false_pressed(self):
        user_answer = "False"
        answer = self.quiz.check_answer(user_answer)
        self.scoreboard.config(text=f"Score: {self.quiz.score}")

        if answer == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.reset)

        self.get_next_question()









