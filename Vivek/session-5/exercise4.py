print("-------------------------------------------------")
print('4) Demonstrate the use of multiple except statement')
print("-------------------------------------------------")

# x = ""
try:
	print(x)
except NameError:
	print('Variable Not Found')
except:
	print('Something Wromg')
