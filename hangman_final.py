#NEW START
#Hangman
import random
list_of_word = ["apple", "barries"]
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
loss = ["h","a","n","g","m","a","n"]
life_remaining_lst = ["_","_","_","_","_","_","_"]
# life_remaining = ""
# for life in life_remaining_lst:
#     life_remaining += "_"
# print(life_remaining)
trail = 0

#while loop to continue  input untill user get the word
while computer_choice_lst != blank_lst and life_remaining_lst != loss:
    guess_word = input("Enter a latter\n").lower()
    remember_value = blank_lst.copy() #every time before changing value of blank this variable will remember the earlier value this cariers
    
    #(User guess a latter  which is their in our word.)
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
        life_remaining_lst[trail-1] = loss[trail-1]
    # print(life_remaining_lst)
    life_remaining = ""
    for life in life_remaining_lst:
        life_remaining += life
    print(life_remaining)