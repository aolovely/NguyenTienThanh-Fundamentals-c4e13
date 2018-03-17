code = {
    "stt" : "siêu tâm trạng",
    "hc" : "học",
    "ng" : "ngu",
    "pt" : "phát triển",
    "eny" : "em người yêu",
    "any" : "anh người yêu",
    "đnn" : "đừng ngu người",
    "lm" : "làm sao"

}

while True:
    for key in code:
        print(key, end ="\t")
    print()
    c = input("your code: ")
    if c in code:
        print("translation: ", code[c])
    else:
        check = input("not found! do you want contribute this word? (Y/N)").upper()
        if check == "Y":
            word = input("enter your translation: ")
            code[c] = word
            print("update")
        elif check == "N":
            break
        else:
            break
