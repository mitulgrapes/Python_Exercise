print(" 2) Print the following pattern")
print("-------------------------------------------------")

def displaytriangle(passval):

	for x in range (1,  passval + 1):
		for y in range (1, x + 1):
			print(y, end=' ')
		print("")

displaytriangle(5)