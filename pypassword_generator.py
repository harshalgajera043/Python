#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#use of random function to choose latters

letters_use = random.sample(letters, nr_letters)
symbols_use = random.sample(symbols, nr_symbols)
numbers_use = random.sample(numbers, nr_numbers)

#concatinate the list to get the list of final charectors and shuffle it
charecter_use = (letters_use+symbols_use+numbers_use)
my_password = ""
for charecter in charecter_use:
  my_password += charecter

print(my_password)
  
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#use of random function to choose latters
letters_use = random.sample(letters, nr_letters)
symbols_use = random.sample(symbols, nr_symbols)
numbers_use = random.sample(numbers, nr_numbers)

#concatinate the list to get the list of final charectors and shuffle it
charecter_use = letters_use+symbols_use+numbers_use
random.shuffle(charecter_use)
print(charecter_use)

#generate the password using string contatination and for loop
password = ""
for charecter in charecter_use:
  password +=charecter
print(password)
