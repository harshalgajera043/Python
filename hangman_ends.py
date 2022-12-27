#NEW START
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
#Hangman
import random
import hangman_words
list_of_word = hangman_words.list_of_word
computer_choice = random.choice(list_of_word)
length = len(computer_choice) #count is used to count number of time a latter occurs in the word
#list of lattter in computer choice
computer_choice_lst = []
for latter in computer_choice:
    computer_choice_lst += latter
# print(computer_choice_lst)

#generate equal number of require blanks (print string)
generate_blanks_str = ""
for letter in computer_choice:
    generate_blanks_str+= "_"
print(generate_blanks_str)
#list of blanks
blank_lst = []
for blank in generate_blanks_str:
    blank_lst += blank
# print(blank_lst)

#game over condition for losser
loss = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
life_remaining_lst = ["_","_","_","_","_","_"]
# life_remaining = ""
# for life in life_remaining_lst:
#     life_remaining += "_"
# print(life_remaining)
trail = 0

#while loop to continue  input untill user get the word
while computer_choice_lst != blank_lst and life_remaining_lst[5] != loss[0]:
    guess_word = input("Enter a latter\n").lower()
    remember_value = blank_lst.copy() #every time before changing value of blank this variable will remember the earlier value this cariers
    #(User guess a latter  which is their in our word.)
    if guess_word in  blank_lst:
        print(f"you already guess the word {guess_word}")
        print(enter_mediate)
    else:
        for i in range(0,length):
            if  guess_word == computer_choice[i]:
                blank_lst[i] = guess_word
        # print(blank_lst)
        enter_mediate = ""
        for char in blank_lst:
            enter_mediate += char
        print(enter_mediate)
        # print(remember_value)
        
        if remember_value == blank_lst:
            trail += 1
            life_remaining_lst[trail-1] = loss[-trail-1]
            print(f"The latter {guess_word}, is not in the word. You loss the life")
        print(life_remaining_lst[trail-1])
    
        # # print(life_remaining_lst)
        # life_remaining = ""
        # for life in life_remaining_lst:
        #     life_remaining += life
        # print(life_remaining)
if computer_choice_lst == blank_lst:
    print("you win")

if life_remaining_lst[5] == loss[0]:
    print(f"You loss, given words is {computer_choice}.")