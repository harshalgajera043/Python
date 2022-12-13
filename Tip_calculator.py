#Tip_calculator
print("Welcome to the tip calculator.")
Bill_amount = input("What is the total bill?\n")
percentage_tip = input("What percentage tip would you like to give? 10,12, or 15?\n")
Number_people = input("How many people to split the bill?\n")

Final_tip = float(Bill_amount)*(1+int(percentage_tip)/100)/int(Number_people)
Final_amount = round(Final_tip,2)
print(f"Each person has to pay: {Final_amount}")