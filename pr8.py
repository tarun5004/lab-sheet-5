# Write a program to find the index of an element in a tuple.

data = input("Enter comma separated values: ")
items = tuple(int(x) for x in data.split())
print("Tuple items: ", items)

element = int(input("Enter the element to find the index: "))
if element in items:
    index = items.index(element)
    print(f"Element {element} found at index {index}.")
else:
    print(f"Element {element} not found in the tuple.")