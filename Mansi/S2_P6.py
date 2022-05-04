#Create tuple with 3 items. Update 2nd item & print all items
Fruits=("Mango","Apple","Grapes")
print("Fruits tuple before updating :",Fruits)
tempList=list(Fruits)
tempList[1] = "Kiwi"
Fruits = tuple(tempList)
print("Updated Tuple",Fruits)