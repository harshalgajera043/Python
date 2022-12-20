
#coin toss test
toss  = input('Enter the "Heads" or "Tails".\n')
final_toss = toss.lower()
print(final_toss)

#validate the inputs
if final_toss == "heads":
    final_toss = 0
elif final_toss == "tails":
    final_toss = 1
else:
    print("Please  enter the currect value of coin toss result.")
print(final_toss)

#use random function to generate the random toss  results
import random
random_result = random.randint(0,1)
# if random_result == 0:
#     random_result = "heads"
# else:
#     random_result = "tails"
print(random_result)

#comparison of calll and random result
if final_toss == random_result:
    print("You won the toss")
elif final_toss !=  random_result:
    print("ohhhh! you loss the toss")
else:
    print("This is not the expected result.")