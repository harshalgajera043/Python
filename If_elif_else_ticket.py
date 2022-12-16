#checker
print("Welcome to the rollerchoaster ride!")
height = int(input("What is you height in cm?\n"))
if height >= 120:
    age = int(input("What is your age?\n")) #will going to ask a person for their age only in the condition if they pass the height criteria.
    if age < 12:
        print("ticket price is $5.")
    elif age <= 18:
        print("ticket price is $7.")
    else:
        print("Your ticket price is $12.")
else:
    print("Go and rise you height if you want to ride aa rollercoaster.")
