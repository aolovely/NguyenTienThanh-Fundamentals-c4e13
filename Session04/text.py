n = [3, -10, 2, 34, 9 ,24, 13]
sor = []

while True:
    minNum = min(n) # for i in range(1, n):
                    #
    sor.append(minNum)
    n.remove(minNum)
    if len(n) == 0:
        break
print(*sor)
