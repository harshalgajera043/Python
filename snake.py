import turtle as t
screen = t.Screen()

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake(t.Turtle):

    def __init__(self):
        self.snake_legth = 3
        self.my_turtle_x_cor = 20
        self.seg_list = []
        super().__init__()

    def snake_display(self):
        for block in range(0, self.snake_legth):
            my_turtle = t.Turtle(shape="square")
            self.seg_list.append(my_turtle)
            my_turtle.penup()
            my_turtle.color("white")
            self.my_turtle_x_cor -= 20
            my_turtle.goto(self.my_turtle_x_cor, 0)
            self.head = self.seg_list[0]

    def snake_move(self):
        for i in range(len(self.seg_list)-1, 0, -1):
            new_x = self.seg_list[i-1].xcor()
            new_y = self.seg_list[i-1].ycor()
            self.seg_list[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # use of listen to control snake direction
    def move_up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(0)

    def extend(self):
        new_segment = t.Turtle()
        my_turtle = t.Turtle(shape="square")
        self.seg_list.append(my_turtle)
        my_turtle.penup()
        my_turtle.color("white")

        new_segment.goto(self.seg_list[-1].position())

