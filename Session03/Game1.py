n = int(input("enter: "))

count = 1
while True:
    if (n//10) != 0:
        count +=1
        n //=10
    else:
        break

print(count)

# while True:
#     count +=1
#     n //=10
#    if n == 0:
#        break
