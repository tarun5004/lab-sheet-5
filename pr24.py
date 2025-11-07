t1 = tuple(input("Enter first tuple: ").split())
t2 = tuple(input("Enter second tuple: ").split())

common = []
for i in t1:
    for j in t2:
        if i == j:
            common.append(i)

print("Common elements:", tuple(common))
