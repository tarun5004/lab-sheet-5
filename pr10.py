#Write a program to repeat a tuple n times

data = input("Enter comma separated values: ")
items = tuple(int(x) for x in data.split())
print("Tuple items: ", items)

n = int(input("Enter the number of times to repeat the tuple: "))
repeated = items * n
print("Repeated tuple: ", repeated)
