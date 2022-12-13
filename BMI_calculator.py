#BMI calculator
#body mass calculator

Enter_Weight = input("What is your weight?\n")
Enter_Height = input("What is your height?\n")
print(type(Enter_Height))
print(type(Enter_Weight))
Body_Mass = float(Enter_Weight)/float(Enter_Height)**2
print("your body mass is " + str(Body_Mass))