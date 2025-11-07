#Write a program to count the occurrences of an element in a tuple.

data = input("Enter comma separated values: ")
items = tuple(int(x)for x in data.split())
print("Tuple items: ",items)

element = int(input("Enter the element to count occurrences: "))
count = 0
for item in items:
    if item == element:
        count += 1
print(f"Element {element} occurs {count} time(s) in the tuple.")