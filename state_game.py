from turtle import Turtle, Screen
from scoreboard import ScoreBoard
import pandas

# Create  screen object
screen = Screen()
screen.setup(740, 510)
screen.title("US States Map Quiz")
image = "/Users/hgaje/PycharmProjects/us-states-game-start/us-states-game-start/blank_states_img.gif"
# screen.addshape(image)
screen.bgpic(image)

# Create turtle object which can write/add state name in case of user make a right guess
write_state_name = Turtle()
# write_state_name.shape(image)
write_state_name.hideturtle()

# let's create score turtle which can be used to  display users present score
score = ScoreBoard()

us_state_map_data = pandas.read_csv("/Users/hgaje/PycharmProjects/us-states-game-start/us-states-game-start/50_states.csv")
state_list = list(us_state_map_data.state)

game_on = True
while game_on:

    if score.current_score == 50:
        game_on = False
    else:
        # Ask user to enter a state name
        user_guess = screen.textinput(title=f"{score.current_score}/50 States Correct",
                                      prompt="Guess a State name: ").title()
        print(user_guess)
        # check for availability of users guess inside our state list
        if user_guess in state_list:
            score.give_point()
            state_list.remove(user_guess)
            current_state = us_state_map_data[us_state_map_data.state == user_guess]
            # print(current_state)
            x_cordinate = int(current_state.x)
            y_cordinate = int(current_state.y)
            write_state_name.penup()
            write_state_name.goto(x_cordinate, y_cordinate)
            write_state_name.write(user_guess)
            # print("Ture")

        elif user_guess == "exit".title():
            for state in state_list:
                current_state = us_state_map_data[us_state_map_data.state == state]
                # print(current_state)
                x_cordinate = int(current_state.x)
                y_cordinate = int(current_state.y)
                write_state_name.penup()
                write_state_name.goto(x_cordinate, y_cordinate)
                write_state_name.write(state)
            game_on = False

# States to remember
remaining_states = "states_to_learn.csv"
state_dict = {}
state_dict["states"] = state_list
remaining_state = pandas.DataFrame(state_dict)
remaining_state.to_csv(remaining_states)



















screen.exitonclick()
