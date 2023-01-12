from turtle import Turtle, colormode, Screen
import random
from move_horizontally import MoveHorizontal
# from color import DotColor
colormode(255)

timmy = Turtle()

vertical_group = 0
timmy.penup()
timmy.goto(-250, -250)

move = MoveHorizontal()

while vertical_group < 5:
    move.move(timmy)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    move.move(timmy)
    timmy.right(90)
    timmy.forward(50)
    timmy.right(90)
    vertical_group += 1















my_screen = Screen()
my_screen.exitonclick()
