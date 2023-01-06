#Higher_Lower
import random
from replit import clear
from game_data import data
from Art import logo, vs

def user_input():
    """This function willl take input from user and return the value of input as a result."""
    value = input("Make a guess on city value. 'A' or 'B'").capitalize()
    if value == "A" or value == "B":
        return value 
    else:
        print("Please enter the valid input!!")
        return user_input()

print(logo)
Choice = random.choice(data)
# print(Choice_1)
name = Choice['name']
occupation = Choice['description']
area = Choice['country']
score = Choice["follower_count"]
print(f"Compare {name}, a {occupation} from {area}.")
data.remove(Choice)

#start of while loop
win_points = 0
win = True
while win==True:
    print(vs)
    
    #make a random choice from updated list after first choice without using function because we have to alot this value to 1st choice variable after the comparison 
    Against_choice = random.choice(data)
    Against_name = Against_choice['name']
    Against_occupation = Against_choice['description']
    Against_area = Against_choice['country']
    Against_score = Against_choice["follower_count"]
    print(f"Against {Against_name}, a {Against_occupation} from {Against_area}.")
    data.remove(Against_choice)
    
    #take input from the user that what they predict about the followers count of both the names
    guess = user_input()
    if guess == "A" and score>=Against_score:
        win_points +=1
        clear()
        print(f"Your current score is {win_points}.")
        name = Against_name
        occupation = Against_occupation
        score = Against_score
        area = Against_area
        print(f"Compare {name}, a {occupation} from {area}.")
    elif guess == "B" and score<=Against_score:
        win_points +=1
        clear()
        print(f"Your current score is {win_points}.")
        name = Against_name
        occupation = Against_occupation
        score = Against_score
        area = Against_area
        print(f"Compare {name}, a {occupation} from {area}.")
    else:
        win = False
        
#Review user score
if win_points > 5:
    print(f"Greaaaat!! {win_points} is excellent score.")
elif win_points > 3:
    print(f"Goooooood!! {win_points} is above avarage score.")
elif win_points > 2:
    print(f"Nooot Bad!! {win_points} is avarage score.")
elif win_points>0:
    print(f"ooooooooo!! {win_points} is too bad.")
elif win_points == 0:
    print("Diaster!! it's seems like you go and comeback with out playing.")