from turtle import Turtle


class AddState(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_on_map(self, state):
        x_cordinate = int(state.x)
        y_cordinate = int(state.y)
        write_state_name.goto(x_cordinate, y_cordinate)
        write_state_name.write(state.state)
