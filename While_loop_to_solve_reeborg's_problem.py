#use of while loop and function to solve reeborg's world problems
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def by_pass():
    turn_right()
    move()
    turn_right()
    move()    

while at_goal() !=  True:
    if wall_on_right() == True:
        if front_is_clear() == True:
            move()
        elif wall_in_front() == True:
            turn_left()
    elif right_is_clear() == True:
        by_pass()
            
while not at_goal():
    if wall_in_front():
        turn_left()
    elif right_is_clear():
        by_pass()
    elif wall_on_right():
        move()
            
            