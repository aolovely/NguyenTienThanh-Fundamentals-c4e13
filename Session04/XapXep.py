n = [3, 4, 0, -3, 5, 9, 34, 23, 2]

for i in range(len(n) - 1):
    for j in range(i + 1, len(n)):
        if n[i] > n[j]:
            a = n[j]
            n[j] = n[i]
            n[i] = a

print(*n)
