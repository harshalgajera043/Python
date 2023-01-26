# list_1 = [1, 2, 3]
# new_list = [item+1 for item in list_1]
# print(new_list)

# new_list = [n*2 for n in range(1, 5)]
# print(new_list)

# new_list = [int(n/2) for n in range(0,10) if n % 2 == 0]
# print(new_list)


# today's final project
# word = ["apple", "ball", "cat", "dog", "elephant", "fan", "gun"]
# alphabat = ["a", "b", "c", "d", "e", "f", "g"]
# name = "abdecaaf"
# list_of_name_word = [word[alphabat.index(letter)] for letter in name]
# print(list_of_name_word)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

result = [number for number in numbers if number % 2 == 0]
print(result)