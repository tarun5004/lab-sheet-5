#Write a program to convert a tuple into a string

data = input("Enter comma separated values: ")
items = tuple(x for x in data.split())
print("Tuple items: ", items)

# Convert tuple to string
items_string = ', '.join(items)
print("String items: ", items_string)
