import turtle
import turtle as t
import random

step_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_race_on = False


def run():
    step = random.randint(0,10)
    return step


def place(turtle_object):
    if turtle_object.xcor() == 900:
        return turtle_object


# taking user input for winner
user_bet = t.textinput("Make you bet", "Which turtle will win the race? Enter the color: ").lower()

screen = t.Screen()
screen.setup(1000, 800)


# Multiple turtle classes
turtle_color_list = ["Red", "Blue", "Yellow", "Green", "Orange"]
Y_position = [300, 150, 0, -150, -300]
my_turtle_list = []

for turtle_object in turtle_color_list:
    New_turtle = t.Turtle(shape="turtle")
    New_turtle.color(turtle_object)
    New_turtle.penup()
    New_turtle.goto(-450, Y_position[turtle_color_list.index(turtle_object)])
    my_turtle_list.append(New_turtle)
# print(my_turtle_list)

# Let's Run
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in my_turtle_list:
        if turtle.xcor() > 450:
            winner = turtle.pencolor().lower()
            if user_bet == winner:
                print(f"ohhhh!! You win the bet.")
            else:
                print(f"You lose!! winner is {winner}.")
            is_race_on = False
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)






# while continue_running:
#     if tim.position() == (450, 300) or timmy.position() == (450, 150) or tip.position() == (450, 0) or tom.position() == (450, -150) or tommy.position() == (450, -300):
#         continue_running = False
#     else:
#         tim.forward(run())
#         timmy.forward(run())
#         tip.forward(run())
#         tom.forward(run())
#         tommy.forward(run())
#
# turtle_list = [tim, timmy, tip, tom, tommy]
# for turtle in turtle_list:
#     winner = place(turtle)
#     print(winner)
#





screen.exitonclick()