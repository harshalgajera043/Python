#Number Guessing Game Objectives:
#computer choice randomint
import random
from art import logo
from replit import clear

def user_input_number():
    """This function takes integer inputs from user in-between 1 and 100"""
    user_number = int(input("Guess a number: "))
    if user_number < 101:
        return user_number
    else:
        # user_number = user_number
        print(f"You have enter {user_number}, please enter a valid number")
        return user_input_number()

def check_for_chance():
    global Number_of_chance
    while not Number_of_chance == 0:
        user_choice = user_input_number()
        if computer_number == user_choice:
            Number_of_chance = 0
            print("You win")
        elif computer_number > user_choice:
            Number_of_chance -=1
            print("Number is too low")
            print(f"You are left with {Number_of_chance}.")
            if Number_of_chance == 0 :
                print(f"Computer choice is {computer_number}. You lose!!")
        elif computer_number < user_choice:
            Number_of_chance -= 1
            print("Number is too high")
            print(f"You are left with {Number_of_chance}.")
            if Number_of_chance == 0 :
                print(f"Computer choice is {computer_number}. You lose!!")

#start of main code
keep_playing = True
while keep_playing:
    print(logo)
    print("I'm think about a number, between '0' and '100'.")
    computer_number = random.randint(0,100)
    # print(f"computer choice is {computer_number}")
    # print("Welcome to number generator!!")
    # print(f"computer choice is {computer_number}")
    # print(user_input_number())
    
    #Ask user for difficulty level
    Difficulty_level = input("Enter the level of difficulty you want to play with.'easy' or 'hard' ").lower()
    Number_of_chance = 0
    if Difficulty_level == "easy":
        Number_of_chance = 10
        print(f"You have {Number_of_chance} chance,You can start making guesses")
    elif Difficulty_level == "hard":
        Number_of_chance = 5
        print(f"You have {Number_of_chance} chance, You can start making guesses")
    
    check_for_chance()
    
    continue_playing = input("Do you want to continue playing? 'y' for Yes and 'n' for No ").lower()
    if continue_playing == 'n':
        keep_playing = False
        print("Thanks for playing!!")
    else:
        clear()
