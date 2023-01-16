from turtle import Screen, Turtle
from scoreboard import ScoreBoard
import food
import snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
game_on = True

# This class creates 3 segment snake
my_snake = snake.Snake()
my_snake.snake_display()

# use of listen to control snake direction
screen.listen()
screen.onkey(key="Up", fun=my_snake.move_up)
screen.onkey(key="Down", fun=my_snake.move_down)
screen.onkey(key="Left", fun=my_snake.move_left)
screen.onkey(key="Right", fun=my_snake.move_right)

food = food.Food()
food.refresh()
score = ScoreBoard()

while game_on:
    screen.update()
    # time.sleep(0.1)
    my_snake.snake_move()

    # Control the speed based on user score
    if score.score < 5:
        my_snake.speed(1)
        time.sleep(0.5)
    elif score.score < 10:
        my_snake.speed(10)
        time.sleep(0.3)
    else:
        my_snake.speed(0)
        time.sleep(0.1)

    # collision with the food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        my_snake.extend()

    # Detect collision with wall
    if my_snake.head.xcor() > 298 or my_snake.head.ycor() > 298 or my_snake.head.xcor() < -298 or my_snake.head.ycor() < -298:
        game_on = False
        score.game_over()

    # Collision with body

    for cor in my_snake.seg_list[1:]:
        if my_snake.head.distance(cor) < 10:
            game_on = False
            score.game_over()









screen.exitonclick()


