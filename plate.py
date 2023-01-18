from turtle import Turtle

PLATE_POSITION_X = [350, -350]

class Plate:
    def __init__(self):
        self.plate_list = []
        self.play_on = True

    def plate(self):
        for position in PLATE_POSITION_X:
            self.hit_plate = Turtle("square")
            self.hit_plate.penup()
            self.hit_plate.color("white")
            self.hit_plate.speed("fastest")
            self.hit_plate.left(90)
            self.hit_plate.shapesize(stretch_wid=1.0, stretch_len=5.0)
            self.hit_plate.goto(position, 0)
            self.plate_list.append(self.hit_plate)

    def plate_up_right(self):
        self.plate_list[0].forward(30)

    def plate_down_right(self):
        self.plate_list[0].backward(30)

    def plate_up_left(self):
        self.plate_list[1].forward(30)

    def plate_down_left(self):
        self.plate_list[1].backward(30)

    # def automove(self):
    #     while self.play_on:
    #         if self.plate_list[1].distance(-370, 285) < 5:
    #             self.plate_list[1].backward(10)
    #         elif self.plate_list[1].distance(-370, -285) < 5:
    #             self.plate_list[1].forward(10)
