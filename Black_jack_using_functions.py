#Blackjack
import random
from replit import clear
from art import logo

#dictionary of card and their respective values!
card_dictionary = {
    "Ace":11,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "Jack":10,
    "Queen":10,
    "King":10,
}

def calculate_score(entry_lst, initial_score):
    """This function import the value of random choice from the card_dictionary and add them. Return total of all the choice in the list"""
    for i in range(0,len(entry_lst)):
        initial_score += card_dictionary[entry_lst[i]]
    return initial_score

#converting all the key from card_dictionary into a list to randomly pick the card from deck.
choice_list = []
for card in card_dictionary:
    choice_list.append(card)


def random_choice(append_list, option_lst):
    """This function will going to randomly pick cards from deck and add them into a append_list"""
    for i in range(0,2):
        choice = random.choice(option_lst)
        append_list.append(choice)
    return append_list

def pick_extra_card(choice_lst, append_list, current_score):
    """This function will going to pick a new card from infinite dack of card and add the point of card into the current score of picker"""
    extra_card = random.choice(choice_lst)
    append_list.append(extra_card)
    print(append_list)
    addition_points = card_dictionary[extra_card]
    return addition_points

def check_for_ace(checking_list, score):
    """This function will gonig to check checling_list if score is greater then 21. If Ace is present in the checking_list then the value of Ace will be changed from 11 to 1"""
    if "Ace" in checking_list:
        score -= 10
    return score


play_blackjack = True
while play_blackjack ==True:
    print(logo)
    #lets start the game
    #pick user cards
    user_card_lst = []
    random_choice(user_card_lst, choice_list)
    print(f"Your cards are {user_card_lst}")
    
    #addition of user cards
    user_score = 0
    user_score += calculate_score(user_card_lst, user_score)
    # print(user_score)
    
    #computer
    #computer cards
    computer_card_lst = []
    random_choice(computer_card_lst, choice_list)
    print(f"Computer card is {random.choice(computer_card_lst)}")
    #computer score
    computer_score = 0
    computer_score += calculate_score(computer_card_lst, computer_score)
    # print(computer_score)
    
    #pick extra card for user
    user_extra_card = input("Do you want to pick an extra card? 'y' for yes and 'n' for No.\n").lower()
    if user_extra_card == 'y':
        user_score += pick_extra_card(choice_list, user_card_lst, user_score)
        # print(user_score)
    # else:
        # print(user_score)
    
    #pick extra card for computer
    if computer_score < 17:
        computer_score += pick_extra_card(choice_list, computer_card_lst, computer_score)
        # print(computer_score)
    # else:
        # print(computer_score)
        
    #chekcing for score greater then 21
    if user_score > 21:
        user_score = check_for_ace(user_card_lst, user_score)
        print(f"Your final score is {user_score}")
    
    if computer_score > 21:
        computer_score = check_for_ace(computer_card_lst, computer_score)
        print(f"Computer score is {computer_score}")
    
    
    #checking for final result of game
    if user_score == computer_score:
        print(f"Score is {user_score} Match draw.")
    elif user_score > computer_score:
        if user_score>21:
            print(f"You excced the 21, your current score is {user_score} against computer score of {computer_score}. You lose")
        else:
            print(f"Your final score is {user_score} against the computer score of {computer_score}. You win")
    else:
        if computer_score > 21:
            print(f"Computer excced the score limit of 21. Your final score is {user_score} against the computer score of {computer_score}. You win!!")
        else:
            print(f"Your score is {user_score} against the computer score of {computer_score}. You lose")

    #looping to keep playing
    continue_playing = input("Do you want to continue playing? type 'y' for yes and 'n' for Exit.\n").lower()
    if continue_playing == 'n':
        play_blackjack = False
        print("Thanks for playing")
    else:
        clear()
        