#. Write a program to find the length of a tuple.

data = input("Enter comma separated values: ")
items = tuple(int(x) for x in data.split())

print("Tuple items: ", items)

count = 0
for item in items:
    count += 1
print("Length of the tuple is:", count)