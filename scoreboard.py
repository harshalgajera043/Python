from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.hideturtle()
        self.goto(190, 230)
        self.display()

    def display(self):
        self.clear()
        self.write(f"current score:{self.current_score}", font=('Courier', 12, 'bold'))
        self.winner()

    def give_point(self):
        self.current_score += 1
        self.display()

    def winner(self):
        if self.current_score == 50:
            self.home()
            self.write("You Win", align="center", font=('Courier', 15, 'bold'))

