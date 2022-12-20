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

import random
random_toss_result = random.randint(1,2)
if random_toss_result == 1:
  print("It\'s a head.")
elif random_toss_result == 2:
  print("It\'s a tail.")