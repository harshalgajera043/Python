from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.right_player_score = 0
        self.left_player_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 230)
        self.write(arg=f"{self.right_player_score}", move=False, align="right", font=('Courier', 48, 'bold'))
        self.goto(-100, 230)
        self.write(arg=f"{self.left_player_score}", move=False, align="left", font=('Courier', 48, 'bold'))


    # R_player_score
    def r_score(self):
        self.right_player_score += 1
        self.update_score()

        # self.goto(100, 230)
        # # self.color("white")
        # # self.penup()
        # self.write(arg=f"{self.right_player_score}", move=False, align="right", font=('Courier', 48, 'bold'))
        # # self.hideturtle()

    def l_score(self):
        self.left_player_score += 1
        self.update_score()

        # self.goto(-100, 230)
        # # self.color("white")
        # # self.penup()
        # self.write(arg=f"{self.left_player_score}", move=False, align="left", font=('Courier', 48, 'bold'))
        # # self.hideturtle()





