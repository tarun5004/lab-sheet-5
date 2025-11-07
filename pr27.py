lst = [tuple(input("Enter pair (like a b): ").split()) for _ in range(3)]

list1 = []
list2 = []
for a, b in lst:
    list1.append(a)
    list2.append(b)

print("First list:", list1)
print("Second list:", list2)
