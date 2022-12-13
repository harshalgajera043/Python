#time_left_calculator

Your_age = int(input("What is your current age?\n"))
Number_of_years_left = 90-Your_age
Number_of_Days_left = Number_of_years_left*365
Number_of_Weeks_left = Number_of_years_left*52
Number_of_Months_left = Number_of_years_left*12
print(f"You have {Number_of_Days_left} days, {Number_of_Weeks_left} weeks, and {Number_of_Months_left} months left")