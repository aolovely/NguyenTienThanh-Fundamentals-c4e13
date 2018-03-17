inventory = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}

inventory["pocket"] = ["seashell", "berry", "lint"]
inventory["backpack"].remove("dagger")
inventory["gold"] += 50

for key, value in inventory.items():
    print(key,": ", value)
