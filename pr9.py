#Write a program to concatenate two tuples.

data1 = input("Enter comma separated values for the first tuple: ")
tuple1 = tuple(int(x) for x in data1.split())
print("First tuple: ", tuple1)

data2 = input("Enter comma separated values for the second tuple: ")
tuple2 = tuple(int(x) for x in data2.split())
print("Second tuple: ", tuple2)

# Concatenate the two tuples
concatenated = tuple1 + tuple2
print("Concatenated tuple: ", concatenated)
