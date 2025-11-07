# Program to convert a tuple of tuples into a dictionary
data = tuple(eval(input("Enter tuple of tuples like ((1,2),(3,4)): ")))

d = {}
for pair in data:
    key = pair[0]
    value = pair[1]
    d[key] = value

print("Dictionary is:", d)
