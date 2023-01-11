from turtle import Turtle, Screen, colormode
colormode(255)

my_turtle = Turtle()


# Challenge No.1
# for i in range(4):
#     my_turtle.forward(100)
#     my_turtle.left(90)

# import heroes

# Challenge No.2
# print(heroes.WORDLIST)
# for i in range(50):
#     my_turtle.pd()
#     my_turtle.forward(10)
#     my_turtle.pu()
#     my_turtle.forward(10)
#     # my_turtle.color("white")
#     # my_turtle.goto(new_x,y)

# # Challenge No.3
# import random
# color_option = ['yellow', 'cyan', 'red', 'light blue', 'pink', 'blue', 'purple', 'green', 'brown', 'orange']
# my_turtle.left(180)
# my_turtle.pensize(3)
# for i in range(3, 11):
#     shape_color = random.choice(color_option)
#     for j in range(i):
#         my_turtle.color(shape_color)
#         my_turtle.forward(50)
#         my_turtle.left(360/i)

# Challenge No.4
# import random
# color_option = ['yellow', 'cyan', 'red', 'light blue', 'pink', 'blue', 'purple', 'green', 'brown', 'orange']
# angle = [0, 90, 180, 270]
# my_turtle.pensize(15)
# my_turtle.speed(0)
# for i in range(250):
#     color = random.choice(color_option)
#     my_turtle.color(color)
#     moving_angle = random.choice(angle)
#     my_turtle.setheading(moving_angle)
#     my_turtle.forward(30)

# Prectice
import random

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, b, g)
#
# angle = [0, 90, 180, 270]
# my_turtle.pensize(15)
# my_turtle.speed(0)
# for i in range(250):
#     code = random_color()
#     my_turtle.color(code)
#     moving_angle = random.choice(angle)
#     my_turtle.setheading(moving_angle)
#     my_turtle.forward(30)

# Challenge No.5
my_turtle.speed("fastest")


def draw_spirogram(angle):

    for i in range(round(360/angle)):
        code = random_color()
        my_turtle.color(code)
        my_turtle.circle(100)
        my_turtle.right(angle)

draw_spirogram(1)







my_screen = Screen()
my_screen.exitonclick()