t1 = tuple(input("Enter first tuple elements: ").split())
t2 = tuple(input("Enter second tuple elements: ").split())

print("Before swapping:", t1, t2)

temp = t1
t1 = t2
t2 = temp

print("After swapping:", t1, t2)
