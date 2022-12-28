# functions with more then one inputs

def function_with_multiple_inputs(height, weights):
    print(f"Your wegiht is {weights} and your height is {height}.")

user_height = input("Enter your height\n")
user_weight = input("Enter your weight\n")

function_with_multiple_inputs(weights = user_weight, height= user_height)