n = [5, 7, 300, 90, 24, 50, 75]

def biggest():
    big = n[0]
    pos = 0
    for i in range(1, len(n)):
        if big < n[i]:
            big = n[i]
            pos = i
    print("now my biggest sheep has size ", big, "let's shear it")
    n[pos] = 8
    print("after shearing, here is my flock: ")
    print(*n, sep=", ")

def grow():
    for j in range(len(n)):
        n[j] += 50
    print("One", i, "has passed, now here is my flock: ")
    print(*n, sep=", ")
def sell():
    total = 0
    for i in range(len(n)):
        total += n[i]
    money = total*2
    print("My flock have in size total : ", total)
    print("i would get", total, "* 2$ = ", money,'$')

print("hello, my name is Love1, and here is my flock: ")
print(*n, sep=", ")
biggest()
for i in range(1, 3):
    grow()
    biggest()
    print("\n")
grow()
sell()
