#Write a Python program to create and display a tuple. 
data = input("Enter comma separated values: ")
items = tuple(int(x)for x in data.split())
print("Tuple items: ",items)
