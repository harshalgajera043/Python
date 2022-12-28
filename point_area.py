import math
def paint_calc(height, width, cover):
    can_require = height*width/cover
    print(math.ceil(can_require))

# Define a function called paint_calc() so that the code below works.   

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

