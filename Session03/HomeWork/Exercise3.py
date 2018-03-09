from random import choice
n = ["champion", "lovely", "cold", "beautiful"]
chon = choice(n)
char = list(chon)

n1= [None]*len(char)
i = 0
while i < len(n1):
    a = choice(char)
    if a in n1:
        continue
    else:
        n1[i] = a
        i += 1

print(*n1, sep =" ")
gus = input("answer: ")
if gus == chon:
    print("yes")
else:
    print("game over")
