
print("1) Print first 10 numbers using for loop \n")
for no in range(1,11):
    print(no)
else:
    print("For loop finished\n")

print("2) Print the pyramid pattern \n")

def DrawPattern(rows):
    k = 0
    for i in range(1, rows+1):
        for space in range(1, (rows-i)+1):
            print(end="  ")
    
        while k!=(2*i-1):
            print("* ", end="")
            k += 1
   
        k = 0
        print()

DrawPattern(5)

print("3) Print all the numbers from 0 to 6 except 3 and  using contunie statement \n")
for no in range(7):
    if(no==3 or no ==6):
        continue
    else:
        print(no)
else:
    print("For loop finished\n")



print("4) Find the price range in which given price is match. Take price =7999  \n")
inputNo = int(input("Take price: "))
if(inputNo>=1000 and inputNo<=5000 ):
    print("Price fall between 1000 to 5000")
elif(inputNo>=5001 and inputNo<=10000 ):
    print("Price fall between 5001 to 10000")
elif(inputNo>=10001 and inputNo<=15000 ):
    print("Price fall between 10001 to 15000")
else:
    print("Price not fall between said range")


print("\n 5) Create a recursive function to print number between 1 to 10 \n")

# k=0
# def PrintNo():
#     if(k>0):
#         nextvalue = k
#         print(nextvalue)

print("\n 6) Create a function which demostrate the use of arbitrary argument \n")

def ArbitaryFun(*hobbies):
  print("My favourite hobby is " + hobbies[2])

ArbitaryFun("Singing","Cricket","Travelling")
