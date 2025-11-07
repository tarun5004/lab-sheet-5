#Write a program to calculate the sum of numeric elements in a tuple

n = int(input("Enter the number of elements in the tuple: "))
elements = []
for i in range(n):
    value = input("enter element:")
    
    if value.isdigit() or (value.replace('.','',1).isdigit() and value.count('.') < 2):
        elements.append(float(value))
    else:
        elements.append(value)
        
t = tuple(elements)
total = 0
for item in t:
    if type(item) == int or type(item) == float:
        total = total + item
print("Tuple items: ", t)
print("Sum of numeric elements in the tuple is:", total)
        