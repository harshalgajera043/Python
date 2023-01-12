from turtle import Turtle, colormode, Screen
import random
import colorgram
from move_horizontally import MoveHorizontal
# from color import DotColor
colormode(255)

# color = colorgram.extract("image.jpg", 50)
#
# color_list = []
# for i in range(0, len(color)):
#     color_object = color[0]
#     r = color_object.rgb.r
#     g = color_object.rgb.g
#     b = color_object.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
# print(color_list)

color_list = [(241, 0, 235), (241, 65, 76), (241, 240, 235), (241, 32, 134), (211, 240, 235), (241, 43, 235), (24, 199, 25), (191, 210, 122), (200, 221, 150), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235), (241, 240, 235)]

timmy = Turtle()
# timmy.shape("turtle")
timmy.speed("fastest")

vertical_group = 0
timmy.penup()
timmy.goto(-250, -250)

move = MoveHorizontal()

while vertical_group < 5:
    move.move(timmy, color_list)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    move.move(timmy, color_list)
    timmy.right(90)
    timmy.forward(50)
    timmy.right(90)
    vertical_group += 1

timmy.hideturtle()













my_screen = Screen()
my_screen.exitonclick()
