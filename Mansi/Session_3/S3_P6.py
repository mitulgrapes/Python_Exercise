#import math

print("6) Create a function which takes milliseconds as parameter & convert it to minutes\n")

def Convert(milliseconds):
	minutes=(millis/(1000*60))%60
	minutes = float(minutes)
	
	print("%f" % (minutes))

millis=int(input("Enter time in milliseconds "))
Convert(millis)	
		