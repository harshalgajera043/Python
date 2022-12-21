
import random
#Use random function to make choice from shuffled list.
participants = input("Enter the all the participants seperated by comma.\n")
participants_list = participants.split(",")
print(participants_list)

#shuffle list
random.shuffle(participants_list)
print(participants_list)

random_choice = random.choice(participants_list)
print(random_choice)

#random_choice for 2 person using random sample
sample_particpants = random.sample(participants_list,2)
print(sample_particpants)