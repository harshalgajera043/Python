
import turtle as t

tim = t.Turtle()
screen = t.Screen()

def tim_move_forwards():
    tim.forward(20)

def tim_move_backwards():
    tim.backward(20)

def tim_rotate_right():
    tim.right(5)

def tim_rotate_left():
    tim.left(5)

def clear_screen():
    tim.reset()

def undo_last():
    tim.undo()

screen.listen()
screen.onkey(key="w", fun=tim_move_forwards)
screen.onkey(key="s", fun=tim_move_backwards)
screen.onkey(key="a", fun=tim_rotate_left)
screen.onkey(key="d", fun=tim_rotate_right)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="e", fun=undo_last)


screen.exitonclick()