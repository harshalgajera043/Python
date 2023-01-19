from turtle import Screen
from car import Car
from player import MyTurtle
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

# My_turtle
turtle = MyTurtle()

screen.listen()
screen.onkey(key="Up", fun=turtle.move_up)

# ScoreBoard class
game_level = ScoreBoard()

# Play_game
game_on = True
list_of_car = []

while game_on:
    time.sleep(game_level.sleep_time)
    screen.update()
    # Creating car object which can be of different random color
    car = Car()
    list_of_car.append(car)
    for car in list_of_car:  # Loop keeping car continuously moving until it reaches -420 on X axis
        if car.xcor() > -420:
            car.move_car()

    # Checking for car and turtle collision
    for car in list_of_car:
        if turtle.distance(car.xcor(), car.ycor()) < 25 and turtle.distance(turtle.xcor(), car.ycor()) < 15:
            game_level.game_over()
            # print(f"ohhoo!! {car} is on me!!😥😭😢😓😞😤😣")
            game_on = False

    game_level.increase_level(turtle)


# continue_playing = screen.textinput(prompt="would you like to continue playing? 'No'/'Yes'",
#                                         title="Continue Playing")
# if continue_playing.lower() == "yes":
#     game_on = True
# else:
#     game_on = False


screen.exitonclick()
