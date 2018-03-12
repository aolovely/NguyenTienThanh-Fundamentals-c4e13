n = input("enter user’s name ")

word = n.strip()

for i in range(len(word)):
    word = word.replace("  ", " ")
list1 = list(word.lower())
list1[0] = list1[0].upper()
for j in range(len(list1)):
    if list1[j] == " ":
        list1[j + 1] = list1[j + 1].upper()

print("Update: ", *list1, sep = "")
