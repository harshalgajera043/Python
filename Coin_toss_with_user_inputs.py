#coin toss with user inputs
import random
toss_call = input('call "Heads" or "Tails.\n"')
final_toss_call = toss_call.lower()
print(final_toss_call)

random_toss_result = random.randint(1,2)
if random_toss_result == 1:
  random_toss_result = "heads"
elif random_toss_result == 2:
  random_toss_result = "tails"
print(random_toss_result)

if random_toss_result == final_toss_call:
  print("You win the toss.")
else:
  print("You loss!")