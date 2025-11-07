#Write a program to access tuple elements using slicing.

data = input("Enter comma separated values: ")
items = tuple(int(x)for x in data.split())
print("Tuple items: ",items)

start = int(input("Enter the start index for slicing (starting from 0): "))
end = int(input("Enter the end index for slicing: "))
if 0 <= start < len(items) and 0 < end <= len(items):
    sliced_item = items[start:end]
    print(f"Sliced tuple from index {start} to {end} is: {sliced_item}")