class MoveHorizontal:

    def color_code(self):
        import random
        self.r = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.g = random.randint(0, 255)
        return (self.r, self.b, self.g)

    def move(self, turtle_object):
        self.horizontal_dot = 0
        while self.horizontal_dot < 10:
            code = self.color_code()
            turtle_object.color(code)
            # turtle_object.forward(50)
            turtle_object.pendown()
            turtle_object.dot(10)
            turtle_object.penup()
            if self.horizontal_dot == 9:
                pass
            else:
                turtle_object.forward(50)
            self.horizontal_dot += 1
