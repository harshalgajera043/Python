from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Ohhoo!! Game over. Your final score is {self.score}.", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()


