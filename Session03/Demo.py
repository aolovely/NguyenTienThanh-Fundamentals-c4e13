from random import choice
s = "champion"
charaters = list("champion")
print(charaters)
random1 = choice(charaters)
print(random1)
n = [None]*len(charaters)

i = 0
while i < len(n):
    a = choice(charaters)
    if a in n:
        continue
    else:
        n[i] = a
        i += 1

print(*n, sep =" ")
gus = input("answer: ")
if gus == s:
    print("yes")
else:
    print("game over")
