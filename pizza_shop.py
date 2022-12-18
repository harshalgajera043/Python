
#pizza order
print("Welcome to my pizza shop!")
bill = 0
pizza_size = input("What size of pizza would like to have? S(small), M(medium) or L(large)\n")
pepperoni = input("Do you want extra pepperoni? Y or N\n")

if pizza_size == "S":
  bill += 15
  if pepperoni == "Y":
    bill +=2

elif pizza_size == "M":
  bill += 20
  if pepperoni == "Y":
    bill +=3

elif pizza_size == "L":
  bill += 25
  if pepperoni == "Y":
    bill +=3

cheese = input("Would you like to have extra cheese ? Y or N\n")

if cheese == "Y":
  bill +=1

print(f"Your final bill is {bill}")