from unicodedata import name


names = ("apple","banana","cherry","orange","kiwi")
y = list(names)
y.append("melon")
y.append("plum")
names = tuple(y)
print(names)