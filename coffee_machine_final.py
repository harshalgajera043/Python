# coffee machine
from coffee_data import MENU, resources
print("Welcome!")


def collector():
    """This function will collect coin of predefine value from operator and return total amount entered"""
    global paid_amount
    range_of_coins = [0.01, 0.05, 0.1, 0.25]
    coin = float(input("please insert the coin: "))
    if coin in range_of_coins:
        paid_amount += coin
        return paid_amount
    else:
        return collector()


def pay_bil(amount):
    """This function will keep asking user to add coin until sum of total added coin don't pass the amount"""
    while not paid_amount >= amount:
        pay = collector()
        if pay == amount:
            print("Please wait we are preparing your order")
        elif pay < amount:
            print(f"You are S{amount - pay} short. Please add coin!!")
        else:
            print(f"Here is your change of ${pay - amount}.")
            print("Please wait we are preparing your order")


# look for resources if enough resource available then only print bill and go ahead
w_available = resources["water"]
m_available = resources["milk"]
c_available = resources["coffee"]
refill = False
while refill == False:
    # Give user option to choose their drink
    coffee = int(input(f"Which coffee would you like to have?\n1.Espresso\n2.Latte\n3.cappuccino\n"))
    if coffee == 1:
        coffee = "espresso"
    elif coffee == 2:
        coffee = "latte"
    else:
        coffee = "cappuccino"
    # print(coffee)

    # require resources
    w_require = MENU[coffee]["ingredients"]["water"]
    if "milk" in MENU[coffee]["ingredients"]:
        m_require = MENU[coffee]["ingredients"]["milk"]
    else:
        m_require = 0
    c_require = MENU[coffee]["ingredients"]["coffee"]

    if w_available >= w_require and m_available >= m_require and c_available >= c_require:
        bill_amount = MENU[coffee]["cost"]
        print(f"Your current bill is: {bill_amount}")
        # will add another other option here later

        # On the basis of user choice print bill and ask user to pay with coins ($0.01, $0.05, $0.1, and $0.25)
        paid_amount = 0
        pay_bil(bill_amount)
        # use while loop until sum total of all the user entry not greater and equal to cost of drink
        # If sum is greater than cost of drink return the change of remaining

        # Make a coffee (Reduce the require resource from available reserve and print the remaining.)
        w_available -= w_require
        m_available -= m_require
        c_available -= c_require
        print(f"water remaining is {w_available}.\nmilk remaining is {m_available}.\ncoffee remaining is {c_available}")
    else:
        print("We are running out of the resources. Please refill the resources!!")
    if w_available <= 0 or m_available <= 0 or c_available <= 0:
        refill = True
        print("We are running out of the resources. Please refill the resources!!")
