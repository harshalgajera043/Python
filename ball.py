from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        # self.ball_y = random.randint(-290, 290)
        # self.ball_angle = random.randint(20, 340)
        # print(self.ball_angle)
        self.color("white")
        self.shape("circle")
        self.speed(0)
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        # self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.home()
        self.bounce_x()

























# from turtle import Turtle
# # import random
#
# class Ball(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         # self.ball_y = random.randint(-290, 290)
#         # self.ball_angle = random.randint(20, 340)
#         # print(self.ball_angle)
#         self.ball = Turtle()
#         self.create_ball()
#         self.x_move = 10
#         self.y_move = 10
#
#     def create_ball(self):
#         self.ball.color("white")
#         self.ball.shape("circle")
#         # self.ball.penup()
#         # self.ball.setheading(self.ball_angle)
#         self.ball.goto(0, 0)
#
#     def move_ball(self):
#         new_y = self.ball.ycor() + self.y_move
#         new_x = self.ball.xcor() + self.x_move
#         self.ball.goto(new_x, new_y)
#
#     def bounce(self):
#         self.y_move *= -1


        # def reflection(self):
        #     if self.ball.xcor() > 0 and self.ball.ycor() > 0:  # 1st
        #         self.right(2 * self.ball_angle)
        #     elif self.ball.xcor() < 0 and self.ball.ycor() > 0:  # 2nd
        #         self.right(2 * self.ball_angle)
        #     elif self.ball.xcor() < 0 and self.ball.ycor() < 0:  # 3rd
        #         self.right(2 * (self.ball_angle-180))
        #     elif self.ball.xcor() > 0 and self.ball.ycor() < 0:  # 4th
        #         self.right((2 * self.ball_angle) - 360)

        # if self.ball.ycor() < 285:
        #    if self.ball.xcor() > 0 and self.ball.ycor() > 0:
        #         self.ball.speed("slowest")
        # elif self.ball.ycor() > 285:
        #     new_y = self.ball.ycor() - 10
        #     new_x = self.ball.xcor() + 10
        #     self.ball.goto(new_x, new_y)
        # elif self.ball.ycor() > -285:
        #     new_y = self.ball.ycor() + 10
        #     new_x = self.ball.xcor() + 10
        #     self.ball.goto(new_x, new_y)
        # elif self.ball.ycor() < -285:
        # # else:
        #     self.setheading(180)
        #     print(self.ball.heading())
        #     # self.ball.forward(10)
