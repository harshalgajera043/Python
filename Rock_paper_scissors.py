# # Day-4
# # import random
# # a = random.randint(1,1000) + random.random()
# # A = round(a,2)
# # print(A)

# import my_module
# D = my_module.B + my_module.C
# print(f"value of D is {D}")
# print(my_module.pi)
# C = random.randint(100,1222)
# # print(C)

#random floating point value between 0 and 5

# import random
# random_integer = random.randint(0,4)
# random_float = random.random()
# random_number = random_integer+random_float
# print(random_number)
# random_final_number = round(random_number,2)
# print(random_final_number)

# import random
# a = random.uniform(0,5)
# print(a)


# #Coin toss with user inputs
# import random
# toss_call = input('call "Heads" or "Tails.\n"')
# final_toss_call = toss_call.lower()
# print(final_toss_call)

# random_toss_result = random.randint(1,2)
# if random_toss_result == 1:
#   random_toss_result = "heads"
# elif random_toss_result == 2:
#   random_toss_result = "tails"
# print(random_toss_result)

# if random_toss_result == final_toss_call:
#   print("You win the toss.")
# else:
#   print("You loss!")

# #coin toss test
# toss  = input('Enter the "Heads" or "Tails".\n')
# final_toss = toss.lower()
# print(final_toss)

# #validate the inputs
# if final_toss == "heads":
#     final_toss = 0
# elif final_toss == "tails":
#     final_toss = 1
# else:
#     print("Please  enter the currect value of coin toss result.")
# print(final_toss)

# #use random function to generate the random toss  results
# import random
# random_result = random.randint(0,1)
# # if random_result == 0:
# #     random_result = "heads"
# # else:
# #     random_result = "tails"
# print(random_result)

# #comparison of calll and random result
# if final_toss == random_result:
#     print("You won the to ss")
# elif final_toss !=  random_result:
#     print("ohhhh! you loss the toss")
# else:
#     print("This is not the expected result.")


# #list

# fruits = ["Grapes","Apple","cherry"]

# #indexing ("In python indexing starts with zero")
# print(fruits[0])
# print(fruits[1:])

# #append function (To add object at the end of the list.)
# fruits.append("beary")
# print(fruits)

# #use of random functionn to chosse a person who will going to pay the bill
# Name  = input("Enter the name of everyone split them by comma\n")
# Name_list = Name.split(",")
# count = len(Name_list)
# Total = count-1
# print(Total)
# print(Name_list)

# import random
# random_person = random.randint(0,Total)
# print(random_person)
# bill_pay = Name_list[random_person]
# print(bill_pay)

# import random
# #Use random function to make choice from shuffled list.
# participants = input("Enter the all the participants seperated by comma.\n")
# participants_list = participants.split(",")
# print(participants_list)

# #shuffle list
# random.shuffle(participants_list)
# print(participants_list)

# random_choice = random.choice(participants_list)
# print(random_choice)

# #random_choice for 2 person using random sample
# sample_particpants = random.sample(participants_list,2)
# print(sample_particpants)

# #Nested list
# My_list1 = ["1","2","3","4",'5',"6","7"]
# My_list2 = [1,2,3,4,5,6,7]
# my_list3 = [My_list1,My_list2]
# print(my_list3)

# #tresure challenge
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")

# position = input("Where do you want to put the treasure? ")

# row = int(position[0])
# column = int(position[1])
# print(row)
# print(column)

# map[row-1][column-1] = "x"

# print(f"{row1}\n{row2}\n{row3}")


#Rock-paper-scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Taking inputs from users
player_choice = input('make you choice "rock", "paper", "scissors".\n').lower()
if player_choice == "rock":
  player_choice = rock
elif player_choice == "paper":
  player_choice = paper
elif player_choice == "scissors":
  player_choice = scissors
else:
  print("please enter valid input.")

print(player_choice)

#use of random function to make a random choice for computer
list_of_outcomes = [rock,paper,scissors]
computer_choice = random.choice(list_of_outcomes)
print(computer_choice)

#comparing user input and computer choice
if computer_choice != player_choice:
  if computer_choice == rock and player_choice == scissors:
    print("You loss")
  elif computer_choice == paper and player_choice == rock:
    print("you loss")
  elif computer_choice == scissors and player_choice == paper:
    print("you loss")
  else:
    print("you win")
else:
  print("match draw")