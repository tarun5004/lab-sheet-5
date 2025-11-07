t = tuple(input("Enter words separated by space: ").split())

max_len = 0
for word in t:
    count = 0
    for ch in word:
        count += 1
    if count > max_len:
        max_len = count

print("Length of the longest word:", max_len)
