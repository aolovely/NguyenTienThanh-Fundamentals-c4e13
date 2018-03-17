prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
}
stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15
}

for key in prices:
    print(key)
    print("price: ", prices[key])
    print("stock: ", stock[key], "\n")

total = 0
for key in prices:
    sell = prices[key] * stock[key]
    total += sell
    print("money you have get from {0} : {1} $".format(key, sell))

print("money your: ", total)
