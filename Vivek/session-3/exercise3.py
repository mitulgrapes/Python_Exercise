print(" 3) Print total odd & even number between 1 to 50")
print("-------------------------------------------------")

num = int(input(" Please Enter any Maximum Number : "))
oddval = ""
evenval = ""
totalodd = 0
totaleven = 0
for number in range(1, num + 1):
    if(number % 2 != 0):
        oddval += "{0} ".format(number)
        totalodd += 1
    else:
    	evenval += "{0} ".format(number)
    	totaleven += 1
print("-------------------------------------------------")
print("Total: " + format(totaleven))
print("Even: " + evenval)
print("-------------------------------------------------")
print("Total: " + format(totalodd))
print("Odd: "+oddval)
print("-------------------------------------------------")