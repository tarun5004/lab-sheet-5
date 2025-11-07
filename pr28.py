t = tuple(input("Enter tuple elements: ").split())

repeated = []
for i in range(len(t)):
    for j in range(i + 1, len(t)):
        if t[i] == t[j] and t[i] not in repeated:
            repeated.append(t[i])

print("Repeated items:", tuple(repeated))
