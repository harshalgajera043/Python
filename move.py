class HorizontalMovement:

    def move(self, color_list, turtle):
        self.number_of_dots = 0
        self.dot_color = ""
        import random
        while self.number_of_dots < 11:
            self.dot_color = random.choice(color_list)
            self.number_of_dots += 1
            turtle.dot(10, self.dot_color)
            turtle.forward(50)

    def change_line_left(self, turtle):
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)

    def change_line_right(self, turtle):
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
