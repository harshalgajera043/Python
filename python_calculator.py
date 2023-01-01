# #calculator
from replit import clear
from art import logo
# print(logo)
# def add(n1,n2):
#     """This function will going to add a number n1 into the number n2."""
#     return n1+n2

# def substract(n1,n2):
#     """This function will going to substract a number n1 from the number n2."""
#     return n1-n2

# def multiple(n1,n2):
#     """This function will going to multiple the number n1 and n2."""
#     return n1*n2

# def divide(n1,n2):
#     """This function will going to divide a number n1 by a number n2."""
#     return n1/n2

# number_1 = float(input("Enter a number.\n")) #first number as input

# further_calculation = True
# while further_calculation:
#     operation = input("+\n-\n*\n/\nWhat operation would you like to perform on both the number?:")
#     number_2 = float(input("Enter a second number.\n")) #Here we take a second number as input inside the while loop so that in each case we can change the number of operation.
#     #will use if/elif/else condition for performaing math operations
#     if operation == "+":
#         result  = add(n1=number_1, n2=number_2)
#     elif operation == "-":
#         result = substract(n1=number_1, n2=number_2)
#     elif operation == "*":
#         result = multiple(n1= number_1, n2=number_2)
#     elif operation == "/":
#         result = divide(n1=number_1 , n2=number_2)
#     print(f"{number_1} {operation} {number_2} = {result}")

#     keep_calculating = input("do you want to keep going with result? press'y' for yes and 'n' for no.\n")
#     if keep_calculating == "n".lower():
#         further_calculation = False
#         clear()
#         print(f"final result is {result}.")
#     else:
#         number_1 = result
#         clear()

#calculator
#addition
def add(n1,n2):
    return n1+n2

#substract
def substract(n1,n2):
    return n1-n2

#multiply
def multiple(n1,n2):
    return n1*n2

#divide
def divide(n1,n2):
    return n1/n2

#operation dictionary
operations = {
    "+":add,
    "-":substract,
    "*":multiple,
    "/":divide,
}

def calculator():
    print(logo)
    
    number_1 = float(input("Enter a first number?\n"))
    
    further_operation = True
    while further_operation == True:
        # print(logo)
        for sign in operations:
            print(sign)
        operator = input("Select anyone operation")
        number_2 = float(input("Enter the second number?\n"))
        result = operations[f"{operator}"](n1=number_1, n2=number_2)
        print(f"{number_1} {operator} {number_2} = {result}")
    
        keep_going = input("Enter 'Y' for  yes and 'N' for no\n").lower()
        if keep_going == "n":
            further_operation = False
            clear()
            print(f"last result is {result}")
            calculator()
        else:
            number_1 = result
            clear()
            print(number_1)

calculator()       
    
    
