# import turtle
# from turtle import Turtle
# from move import HorizontalMovement
# import random
#
# timmy = Turtle()
# colour = ['red', 'yellow', 'blue', 'pink', 'black', 'white']
# dot_number = 0
#
# move = HorizontalMovement()
# vertical_line = 0
# timmy.color("white")
# timmy.goto(-250, -250)
# while vertical_line < 5:
#     move.move(colour, timmy)
#     move.change_line_left(timmy)
#     move.move(colour, timmy)
#     move.change_line_right(timmy)
#     vertical_line += 1
#
#
# my_screen = turtle.exitonclick()
# my_screen

from turtle import Turtle, Screen

my_turtle = Turtle()
for i in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)







my_screen = Screen()
my_screen.exitonclick()