t = tuple(input("Enter tuple elements: ").split())

same = True
first = t[0]
for i in t:
    if i != first:
        same = False

if same:
    print("All elements are same")
else:
    print("Elements are not same")
