# #for loop
# fruits =["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
# print(fruits)

# #calculate the avarage height of the class
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n]) #converting inputs into integer using python loops

# sum_input = sum(student_heights)
# total_number_of_students = len(student_heights)
# avrage_height  = sum_input/total_number_of_students
# print(round(avrage_height))

# #calculate the avarage height of the class
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n]) #converting inputs into integer using python loops

# #calculate the total number of elements in the list using for loop
# total_number_of_student = 0
# for n in student_heights:
#   total_number_of_student += 1
# print(total_number_of_student)

# #sum of all the elements in the list
# student_height = 0
# for height in student_heights:
#   student_height = student_height + height
# #here we are using print out side the for loop because we want sum to  be printed out only after all the iteration of the loop
# print(student_height)

# #avarage height
# avarage_height = student_height/total_number_of_student
# print(round(avarage_height))

# #maximum score
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# # maximum_score = max(student_scores)
# # print(f"The highest score in the class is: {maximum_score}")

# #using for loop
# maximum_score = 0
# for score in student_scores:
#   if score> maximum_score:
#     maximum_score = score
# print(f"The highest score in the class is: {maximum_score}")

#surm of 1 to 100 using range
# #mathod_1
# total = 0
# for n in range(0,101,1):
#   total += n
# print(total)

# #mathod_2
# my_list = []
# for n in range(1,101,1):
#   my_list.append(n)

# number_sum = 0
# for number in my_list:
#   number_sum += number
# print(number_sum)

#even_sum

#method_1 using simple for loop and range function
even_sum = 0
for n in range(2,101,2):
    even_sum += n
print(even_sum)

#method_2 first create list using append and then using for loop
my_list = []
for n  in range(2,101,2):
  my_list.append(n)
even_sum = 0
for number in my_list:
  even_sum += number
print(even_sum)

#method_3 combination of for loop and if/else condition to differentiate even and odd numbers
even_sum = 0
for n in range(0,101):
  if n%2 == 0:
    even_sum += n
print(even_sum)
