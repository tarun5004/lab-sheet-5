# Program to remove duplicates from a tuple without using set()
t = tuple(input("Enter tuple elements separated by space: ").split())

# Removing duplicates manually
unique = []
for item in t:
    if item not in unique:
        unique.append(item)

# Converting back to tuple
t_no_dup = tuple(unique)
print("Tuple after removing duplicates:", t_no_dup)
