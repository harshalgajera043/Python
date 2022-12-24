#calculate the avarage height of the class
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) #converting inputs into integer using python loops

sum_input = sum(student_heights)
total_number_of_students = len(student_heights)
avrage_height  = sum_input/total_number_of_students
print(avrage_height)