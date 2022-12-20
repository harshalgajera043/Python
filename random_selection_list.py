
#use of random functionn to chosse a person who will going to pay the bill
Name  = input("Enter the name of everyone split them by comma\n")
Name_list = Name.split(",")
count = len(Name_list)
Total = count-1
print(Total)
print(Name_list)

import random
random_person = random.randint(0,Total)
print(random_person)
bill_pay = Name_list[random_person]
print(bill_pay)