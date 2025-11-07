#2. Write a program to create a tuple with different data types

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
is_student = input("Are you a student (yes/no)? ").strip().lower() == 'yes'

tuple_data = (name, age, height, is_student)
print("Tuple with different data types:", tuple_data)