n = ["love1", "love2", "love3"]

# for i in range(len(n)):
#     print(i+1,". ", n[i], sep="")
for index, item in enumerate(n):
    print(index, ", ", item, sep ="")
print("*"*10)
for item in n:
    print(item)
n[0] = "love4"
print(n[0])
