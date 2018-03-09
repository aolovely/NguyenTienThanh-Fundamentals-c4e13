clothes = ["T-Shirt", "Sweater"]

def Read():
    print("Our items: ")
    for index, item in enumerate(clothes):
        print(index + 1,".", item, sep="")
def Creat():
    clothes.append(input("Enter new item: "))
def Update():
    pos = int(input("Update position: "))
    if pos <= len(clothes):
        clothes[pos - 1] = input("New item: ")
    else:
        print("position is not available")
def Delete():
    pos1 = int(input("position delete: "))
    if pos1 <= len(clothes):
        del clothes[pos1 - 1]
    else:
        print("position is not available")

while True:
    a = input("welcome to our shop, what do you want? (C R U D): ")
    a = a.upper()
    if a == "C":
        Creat()
        Read()
        print("to exit please press E")
    elif a == "R":
        Read()
        print("to exit please press E")
    elif a == "U":
        Update()
        Read()
        print("to exit please press E")
    elif a == "D":
        Delete()
        Read()
        print("to exit please press E")
    elif a == "E":
        break
    else:
        print("Not valid, please re-enter")
