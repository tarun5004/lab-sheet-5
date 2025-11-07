#Write a program to access tuple elements using indexing.

data = input("Enter comma separated values: ")
items = tuple(int(x) for x in data.split())
print("Tuple items: ", items)

index = int(input("Enter the index of the element you want to access (starting from 0): "))
if 0 <= index < len(items):
    print(f"Element at index {index} is: {items[index]}")
else:
    print("Index out of range.")