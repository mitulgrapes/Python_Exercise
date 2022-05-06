#Create tuple with 5 items & add other 2 new items and then print all items
latters=("a","b","c","d","e")
print("latters tuple before adding :",latters)
tempList=list(latters)
tempList[5] = "f"
tempList[6] = "g"
latters = tuple(tempList)
print("Updated Tuple",latters)
