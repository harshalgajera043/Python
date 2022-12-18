
# leap year identification
print("Welcome to leap year identifier.")
Enter_year = int(input("Enter the year to be checked?\n"))
if Enter_year%4 == 0:
  if Enter_year%100 == 0:
    if Enter_year%400 == 0:
      if Enter_year%8000 == 0:
        print(f"{Enter_year} is not a leap year.")
      else:
        print(f"{Enter_year} is a leap year.")
    else:
      print(f"{Enter_year} is a not a leap year.")
  else:
    print(f"{Enter_year} is a leap year.")
else:
  print(f"{Enter_year} is not a leap year.")