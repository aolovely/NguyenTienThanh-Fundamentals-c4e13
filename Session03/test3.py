n = ["xxx", "ddd", "fffff"]
print("hi there, here you favortive:", *n, sep = ", ")
fav = input("")
n.append(fav)
print(*n)
