############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
from replit import clear
from art import logo
user_score = 0
def user_score(card_lst):
    user_score = 0
    for i in range(0,len(card_lst)):
        user_score += card_dictionary[card_lst[i]]
    return user_score
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
# continue_game = input("Do you want to play blackjack? type 'y' for yes and 'n' for no.\n")

#creating list of all the possible card so that using random module we can peak card from this list.
#will going to use those card and dictionary to get the value of card from dictionary.
def blackjack():
    print(logo)
    card_lst = []
    for card in card_dictionary:
        card_lst.append(card)
    # print(card_lst)
    
    #participants cards
    User_card_lst = []
    for i in range(0,2):
        user = random.choice(card_lst)
        User_card_lst.append(user)
    final_user_score = user_score(User_card_lst)
    print(f"Your cards {User_card_lst} Current Score: {final_user_score}")
    #lets use this random choice as key to get the value of those cards.
    # user_score()
    # user_score = 0
    # for i in range(0,len(User_card_lst)):
    #     user_score += card_dictionary[User_card_lst[i]]
    # print(user_score)
        
    #computer cards
    computer_card_lst = []
    for i in range(0,2):
        computer_choice = random.choice(card_lst)
        computer_card_lst.append(computer_choice)
    # print(computer_card_lst)
    print(f"Computer card: {random.choice(computer_card_lst)} and * ")
    computer_score = 0
    for i in range(0,len(computer_card_lst)):
        computer_score += card_dictionary[computer_card_lst[i]]
    # print(computer_score)
    
    add_card = input("Do you want to peak another card? 'y' for yes 'n' for no\n").lower()
    if add_card =="y":
        User_card_lst.append(random.choice(card_lst))
        final_user_score = user_score(User_card_lst)
        print(f"Your final score is {final_user_score}")
    # else:
    #     print(final_user_score)
    # print(f"computer final score is {computer_score}")
    # print(f"your final cards {User_card_lst}")
    # print(f"computer final cards {computer_card_lst}")
    
    if "Ace" in User_card_lst and final_user_score>21:
        final_user_score -= 10
    if "Ace" in computer_card_lst and computer_score>21:
        computer_score -= 10

    print(f"computer final score is {computer_score}")
    # print(f"your final cards {User_card_lst}")
    # print(f"computer final cards {computer_card_lst}")
    print(f"Your final score is {final_user_score}")
    
    if (final_user_score > 21 and computer_score>21) or final_user_score == computer_score:
        print("Match Draw")
    elif final_user_score > computer_score:
        if final_user_score>21:
            print("You loss.")
        else:
            print("You win!!")
    elif not final_user_score > computer_score:
        if final_user_score>21:
            print("You win!!")
        else:
            print("You loss.")
            
    want_to_continue_playing ="" #looping using recursive functions
    want_to_continue_playing = input("Do you want to continue playing? type 'y' for yes and 'n' for no\n").lower()
    if want_to_continue_playing == "y":
        clear()
        blackjack() #To add recursiveness in this code we have used blackjack function inside blackjack function which will going to continue until recursion condition turns false.

blackjack()