 # string formating: answer = input("is {0} your number?".format(mid))
print("guess your number ")
input("Now think a number from 0 to 100, then press 'enter'")
print('''
all you have to is answer to mu guess
'c' if my guess is 'C'orrect
'L' if my guess is
''')
low = 0
hight = 101

while True:
    mid = (low + hight)//2
    answer = input("is {0} your number?".format(mid).lower())

    if answer == "c":
        print("i knew it")
        break
    elif answer == "s":
        low = mid
    else answer == "l":
        hight = mid
