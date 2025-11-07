#Write a program to find the maximum and minimum values in a tuple 
data = input("Enter comma separated values: ")
items = tuple(int(x) for x in data.split())
print("Tuple items: ", items)

# Find maximum and minimum values
max_value = 0
min_value = 0
for i in items:
    if i > max_value:
        max_value = i
    if min_value == 0 or i < min_value:
        min_value = i
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")