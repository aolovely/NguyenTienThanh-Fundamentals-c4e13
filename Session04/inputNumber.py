n = input("enter a sequence of number, separted by space: ")
print(n.strip().split(" ")) # strip( cat dau cach thua o dau va cuoi)
# words = s.strip().split()
# number = []
# for item in words:
#     number.append(int(item))
list2 = [int(i) for i in n.split()]
print(list2)
check = 1
for i in range(len(list2) - 1):
    if list2[i] > list2[i + 1]:
        check = 0
        break
if check:
    print("your sequence is yet")
else:
    print("your sequence is not yet")
    for i in range(len(list2) - 1):
        for j in range(i + 1, len(list2)):
            if list2[i] > list2[j]:
                a = list2[j]
                list2[j] = list2[i]
                list2[i] = a
    print("****", *list2)
