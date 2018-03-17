# persion = ["quy", 20, 0, "ha noi", ["coding"]]
# dictionary
person = {
    "name" : "love", # ~ key ; value
    "age" : "20",
    "ex" : "80"
}
print(person)
print(person["age"])
key = "age"
if key in person:
    print(person[key])
else:
    print("not found")

for key in person:
    print(key, person[key])

for value in person.values():
    print(value)
for key, value in person.items():
    print(key, value)
# for k in person.items():
#     print(k)

person["age"] = 3
person["vx"] = "40"
print(person)
