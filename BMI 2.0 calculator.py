height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

Actual_BMI = weight/height**2
BMI = round(Actual_BMI)
if BMI<=18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI<=25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI<=30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI <= 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print("Your BMI is {BMI}, you are clinically obese.")
