# Program to check if two tuples are equal
t1 = tuple(input("Enter elements of first tuple separated by space: ").split())
t2 = tuple(input("Enter elements of second tuple separated by space: ").split())

# Logic: Check if both tuples are same
if t1 == t2:
    print("Both tuples are equal")
else:
    print("Tuples are not equal")
