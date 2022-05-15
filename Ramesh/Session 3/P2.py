# Print the following pattern

def printTriangle(rows):
	for i in range(1, rows + 1):
	    for j in range(1, i + 1):
	        print(j, end=' ')
	    print('')
n = 5
printTriangle(n)
