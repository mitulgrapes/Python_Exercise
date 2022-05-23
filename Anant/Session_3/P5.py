#Create recursive function to print number between 1 to 10

def printRecu(n):
    if n>1:
        printRecu(n-1)
    print(n, end=" ")
        
n=int(input("Please Enter Number="))

printRecu(n)
