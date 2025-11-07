t1 = tuple(input("Enter first tuple: ").split())
t2 = tuple(input("Enter second tuple: ").split())

diff = []
for i in t1:
    found = False
    for j in t2:
        if i == j:
            found = True
    if not found:
        diff.append(i)

print("Difference (elements in t1 but not in t2):", tuple(diff))
