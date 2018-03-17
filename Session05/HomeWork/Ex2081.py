strings = input("enter a string ").lower()

strings = strings.replace(" ", "")
letters = {}
for letter in strings:
    letters[letter] = strings.count(letter)

letterItem = list(letters.items())
letterItem.sort()
letterItem = dict(letterItem)

for key, value in letterItem.items():
  print(key, value)
