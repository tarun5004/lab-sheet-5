#Write a program to check if an element exists in a tuple.

data = input("Enter comma separated values: ")
items = tuple(int(x)for x in data.split())
print("Tuple items: ",items)

element = int(input("Enter the element to check for existence: "))
if element in items:
     print(f"Element {element} exists in the tuple.")
else:
    print(f"Element {element} does not exist in the tuple.")