nested = ((1, 2), (3, 4), (5, (6, 7)))
flat = []

for i in nested:
    for j in i:
        if type(j) == tuple:
            for k in j:
                flat.append(k)
        else:
            flat.append(j)

print("Flattened tuple:", tuple(flat))
