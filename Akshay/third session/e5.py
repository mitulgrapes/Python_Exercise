# Create recursive function to print number between 1 to 10
n = int(input())

def rec(n):
    if n==0:
        print(0)
    else:
        print(-n)
        rec(n-1)
        print(n)

rec(n)                                                                                                                                                                                                                                                                                                                                         # Create recursive function to print number between 1 to 10
n = int(input())

def rec(n):
    if n==0:
        print(0)
    else:
        print(-n)
        rec(n-1)
        print(n)

rec(n)