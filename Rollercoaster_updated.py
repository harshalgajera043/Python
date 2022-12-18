
#checker
print("Welcome to the rollerchoaster ride!")
height = int(input("What is you height in cm?\n"))
bill = 0
if height >= 120:
    age = int(input("What is your age?\n")) #will going to ask a person for their age only in the condition if they pass the height criteria.
    if age < 12:
      bill = 5
      print("Child tickets are $5.")
    elif age <= 18:
      bill = 7
      print("Youth tickets are $7.")
    else:
      bill = 12
      print("Adult tickets are $12.")
    Want_photo = input("Do you want to take photo? Y or N\n")
    if Want_photo == "Y":
      # add $3 in their bill
      bill += 3
      print(f"Your final bill is {bill}")
    else:
      print(f"Your fill bill is {bill}")
else:
    print("Go and rise you height if you want to ride aa rollercoaster.")

  
#checker
print("Welcome to the rollerchoaster ride!")
height = int(input("What is you height in cm?\n"))
bill = 0
if height >= 120:
  Want_photo = input("Do you want to take a photo? Y or N\n")
  if Want_photo == "Y":
    bill += 3
  age = int(input("What is your age?\n")) #will going to ask a person for their age only in the condition if they pass the height criteria.
  if age < 12:
    bill += 5
  elif age <= 18:
    bill += 7 
  else:
    bill += 12
  print(f"Your final bill is {bill}")
else:
    print("Go and rise you height if you want to ride aa rollercoaster.")