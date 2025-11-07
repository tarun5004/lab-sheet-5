#Write a program to reverse a tuple.
data = input("Enter comma separated values: ")
items = tuple(x for x in data.split(","))

# Reverse the tuple without using built-in functions and slicing
reversed_items = ()
for i in range(len(items)-1, -1, -1):
    reversed_items += (items[i],)