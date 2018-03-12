n = input("enter your balace: ")

n =n.lower()
n = n.title()
n = n.strip()
for i in range(len(n)):
    n = n.replace('  ', ' ',)

print("your updated balace: ", n )
