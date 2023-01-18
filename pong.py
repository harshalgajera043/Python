from turtle import Screen
from plate import Plate
from court import Court
from ball import Ball
from score import ScoreBoard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("ENJOY PONG!!")
screen.tracer(0)

# Plate
plate = Plate()
plate.plate()
r_plate = plate.plate_list[0]
l_plate = plate.plate_list[1]
# print(r_plate)

# Boundry_court
center = Court()
center.court()

# Create Ball
main_ball = Ball()
# main_ball.create_ball()

# Score
score = ScoreBoard()

# controlling plate using keyboard
screen.listen()
screen.onkey(key="w", fun=plate.plate_up_left)  # Multiuser Game
screen.onkey(key="s", fun=plate.plate_down_left)  # Multiuser Game
screen.onkey(key="Up", fun=plate.plate_up_right)
screen.onkey(key="Down", fun=plate.plate_down_right)
# screen.update()

game_on = True
l_player_score = 0
r_player_score = 0
sleep_time = 0.3
while game_on:
    screen.update()
    time.sleep(sleep_time)
    main_ball.move()

    # Detect collision with up or bottom wall
    if main_ball.ycor() > 280 or main_ball.ycor() < -280:
        main_ball.bounce_y()

    # Detect collsion with plate(right)
    if r_plate.distance(main_ball) < 50 and main_ball.xcor() > 320:
        main_ball.bounce_x()
        sleep_time *= 0.6


    # Detect collsion with plate(left)
    if l_plate.distance(main_ball) < 50 and main_ball.xcor() < -320:
        main_ball.bounce_x()
        sleep_time *= 0.6

    # Ball misses the plate
    # Right
    if main_ball.xcor() > 370:
        # print("Missssses")
        score.l_score()
        # l_player_score += 1
        # print(f"Left side player score is: {l_player_score}")
        main_ball.reset_position()
        sleep_time = 0.3
    # Left
    elif main_ball.xcor() < -370:
        # print("Missed")
        score.r_score()
        # r_player_score += 1
        # print(f"Right side player score is: {r_player_score}")
        main_ball.reset_position()
        sleep_time = 0.3

    if score.right_player_score == 10:
        score.goto(0,0)
        score.write("Right side player win the game", move=False, align="center", font=('Courier', 28, 'bold'))
        game_on = False
    elif score.left_player_score == 10:
        score.goto(0, 0)
        score.write("left side player win the game", move=False, align="center", font=('Courier', 28, 'bold'))
        game_on = False

screen.exitonclick()
