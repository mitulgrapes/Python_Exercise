# Create tuple with 3 items. Update 2nd item & print all items
thistuple = ("apple", "banana", "cherry")

thislist = list(thistuple)
thislist[1] = "mango"

thistuple = tuple(thislist)
print(thistuple)