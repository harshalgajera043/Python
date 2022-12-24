
#calculate the avarage height of the class
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) #converting inputs into integer using python loops

#calculate the total number of elements in the list using for loop
total_number_of_student = 0
for n in student_heights:
  total_number_of_student += 1
print(total_number_of_student)

#sum of all the elements in the list
student_height = 0
for height in student_heights:
  student_height = student_height + height
print(student_height)

#avarage height
avarage_height = student_height/total_number_of_student
print(round(avarage_height))