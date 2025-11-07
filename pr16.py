#Write a program to sort a tuple of strings alphabetically

n = int(input("Enter the number of elements in the tuple: "))
elements = []
for i in range(n):
    value = input("enter element:")
    elements.append(value)

t = tuple(elements)
print("Tuple items: ", t)

# Sort the tuple of strings
sorted_elements = list(t)
for i in range(len(sorted_elements)):
    for j in range(i + 1, len(sorted_elements)):
        if sorted_elements[i] > sorted_elements[j]:
            # Swap
            temp = sorted_elements[i]
            sorted_elements[i] = sorted_elements[j]
            sorted_elements[j] = temp
sorted_tuple = tuple(sorted_elements)
print("Sorted tuple items: ", sorted_tuple)
