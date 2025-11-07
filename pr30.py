t1 = tuple(map(int, input("Enter first tuple of numbers: ").split()))
t2 = tuple(map(int, input("Enter second tuple of numbers: ").split()))

sum_tuple = []
for i in range(len(t1)):
    sum_tuple.append(t1[i] + t2[i])

print("Element-wise sum:", tuple(sum_tuple))
