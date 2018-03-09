n = ["love1", "love2", "love3"]
print("hi there, here you favorite things so far: ")
for index, item in enumerate(n):
    print(index + 1, ", ", item, sep ="")
# a = int(input("position you want update: "))
# n[a - 1] = input(" your favortave:")
# print("your replacing favortave? ")
# for index, item in enumerate(n):
#     print(index +1 , ", ", item, sep ="")

a = int(input("position your want o get rid of? "))

del n[a - 1] # n.pop(a - 1) dung de xoa theo vi tri
# xoa theo ten dung removete
deleteName = input("favorite: ")
n.remove(deleteName)
# xem gia tri co trong list k thi xoa
if deleteName in n:  # theo index dung  if a in len(n):
    n.remove(deleteName)
else:
    print("not found")
for index, item in enumerate(n):
    print(index + 1, ", ", item, sep ="")
