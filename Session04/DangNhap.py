print("hi there, this is a superuser ")
use = "love"
pass1 = "love1"
i = 0
j = 0
while i < 3:
    n = input("userName: ")
    if n == use:
        while j < 3:
            k = input("passWord: ")
            if k == pass1:
                print("wellcome")
                break
            else:
                print("passWork is incorrect")
            j += 1
            if j == 3:
                print("you filed pass")
                break
        break

    else:
        print("you are not superuse")
    i += 1
    if i == 3:
        print("you log 3 time")
        break
