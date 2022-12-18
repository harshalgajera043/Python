
#Lover checker
print("Welcome to the love checker!")
Name_1 = input("Enter the name of 1st partner.\n")
Name_2 = input("Enter the name of 2nd partner.\n")
name_1 = Name_1.lower()
name_2 = Name_2.lower()

#count true
Count_T_1 = name_1.count("t")
Count_R_1 = name_1.count("r")
Count_U_1 = name_1.count("u")
Count_E_1 = name_1.count("e")

Count_T_2 = name_2.count("t")
Count_R_2 = name_2.count("r")
Count_U_2 = name_2.count("u")
Count_E_2 = name_2.count("e")

Total_True_Name_1 = Count_T_1 + Count_R_1 + Count_U_1 + Count_E_1
Total_True_Name_2 = Count_T_2 + Count_R_2 + Count_U_2 + Count_E_2

Total_True = Total_True_Name_1+Total_True_Name_2

#count love

Count_L_3 = name_1.count("l")
Count_O_3 = name_1.count("o")
Count_V_3 = name_1.count("v")
Count_E_3 = name_1.count("e")

Count_L_4 = name_2.count("l")
Count_O_4 = name_2.count("o")
Count_V_4 = name_2.count("v")
Count_E_4 = name_2.count("e")

Count_Lover_Name_1 = Count_L_3 + Count_O_3 + Count_V_3 + Count_E_3
Count_Lover_Name_2 = Count_L_4 + Count_O_4 + Count_V_4 + Count_E_4

Count_Lover = Count_Lover_Name_1 + Count_Lover_Name_2

Total_score = Total_True*10 + Count_Lover

if Total_score <= 10 or Total_score >= 90:
  print(f"Your score is {Total_score}, you go together like coke and mentos.")
elif Total_score >= 40 and Total_score<=50:
  print(f"Your score is {Total_score}, you are alright together.")
else:
  print(f"your score is {Total_score}")