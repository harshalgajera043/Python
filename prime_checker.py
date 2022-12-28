#prime checeker
def prime_checker(number):
    division_list = []
    for i in range(1,number):
        if number%i == 0:
            division_list.append(number)
    if len(division_list) == 1:
        print(f"{number} It\'s a prime number.")
    else:
        print(f"{number} It\'s not a prime number.")
    

# n = int(input("Check this number: "))
for number in range(0,101):
    n = number
    prime_checker(number=n)
