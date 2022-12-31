#function
#title() can be used to convert our string into a titlecase which change the input "hARsHal" into "Harshal".
f_name = input("Enter your firstname.\n").title()
s_name = input("Enter your surname\n").title()

def formate_name(firstname, surname):
    if firstname == "" or surname == "":
        return "please provide valid inputs."
    return f"{firstname} {surname}."

print(formate_name(firstname =f_name, surname = s_name))