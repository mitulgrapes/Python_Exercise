#
#Example file for working with conditional statement
#
def main():
	#x,y =8,8
	x= int(input("Enter Value for X : \n"))
	y = int(input("Enter value for Y : \n"))
	
	if(x < y):
		st= "x is less than y"
	
	elif (x == y):
		st= "x is same as y"
	
	else:
		st="x is greater than y"
	print(st)
	
if __name__ == "__main__":
	main()