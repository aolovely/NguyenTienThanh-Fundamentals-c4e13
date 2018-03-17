map1 = {
    "x" : 5,
    "y" : 5,

}
#
# for y in range(map1["y"]):
#     for x in range(map1["x"]):
#         print("-", end =" ")
#     print()

player = {
    "x" : 0,
    "y" : 4,
}

boxes = [
    {"x" : 1, "y" : 1},
    {"x" : 2, "y" : 2},
    {"x" : 3, "y" : 3},
]
des = [
    {"x" : 2, "y" : 1},
    {"x" : 3, "y" : 2},
    {"x" : 4, "y" : 3},

]
while True:
    for y in range(map1["y"]):
        for x in range(map1["x"]):

            desIsHere = False
            for des1 in des:
                if des1["x"] == x and des1["y"] == y:

                    desIsHere = True
                    break

            boxIshere = False
            for box in boxes:
                if box["x"] == x and box["y"] == y:

                    boxIshere = True
                    break

            playerIsHere = False
            if x == player["x"] and y == player["y"]:
                playerIsHere = True

            if boxIshere:
                print("B", end = " ")
            elif playerIsHere:
                print("p", end = " ")
            elif desIsHere:
                print("D", end = " ")
            else:
                print("-", end = " ")

        print()
    Win = True
    for box in boxes:
        if box not in des:
            Win = False
    if Win:
        print("you win")
        break
    move = input("your move? ").upper()
    dx = 0
    dy = 0
    if move == "W":
        dy = -1

    elif move == "S":
        dy = 1

    elif move == "A":
        dx = -1

    elif move == "D":
        dx = 1

    if  0 <= player["x"] + dx < map1["x"] and 0 <= player["y"] + dy < map1["y"]:
        player["x"] += dx
        player["y"] += dy
    for box1 in boxes:
        if box1["x"] == player["x"] and box1["y"] == player["y"]:
            if 0 <= box1["x"] + dx < map1["x"] and 0 <= box1["y"] + dy < map1["y"]:
                box1["x"] += dx
                box1["y"] += dy
