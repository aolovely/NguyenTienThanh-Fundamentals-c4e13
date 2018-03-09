from random import randint
n = randint(0, 100)
count = 0
while True:
    a = int(input("enter: "))
    count +=1
    if a == n:
        print("you win ")
        break
    elif a < n:
        print("Too small:( ")
    else:
        print("a litle too large")
    if count == 7:
        print("game over")
        break
