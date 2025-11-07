#Write a program to convert a list into a tuple.

data = input("Enter comma separated values: ")
items = [int(x) for x in data.split()]
print("List items: ", items)

# Convert list to tuple
items_tuple = tuple(items)
print("Tuple items: ", items_tuple)
