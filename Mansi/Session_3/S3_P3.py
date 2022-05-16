print("3) Print total odd & even number between 1 to 50\n")

print("All Even Numbers Beetween 1 to 50 : \n")
for num in range(1,50):
     
    # checking condition
    if num % 2 == 0:
        print(num, end = " ")
		
print("\n\nAll Odd Numbers Between 1 to 50 : \n")
for num in range(1,50):
	
	if num % 2 != 0:
		print(num,end = " ")

	
