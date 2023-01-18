from turtle import Turtle


class Court:

    def __init__(self):
        super().__init__()
        self.current_y = -280

    def court(self):
        while self.current_y < 300:
            self.wall_piece = Turtle()
            self.wall_piece.penup()
            self.wall_piece.shapesize(stretch_wid=0.7, stretch_len=0.2)
            self.wall_piece.color("white")
            self.wall_piece.shape("square")
            self.wall_piece.goto(0, self.current_y)
            self.current_y += 30
