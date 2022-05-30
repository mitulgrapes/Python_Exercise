print("4) Create module which convert MB to GB.\n")

def convert(value):
	gb = value / 1024
	#print("Converted "+ value + "to GB: " + gb)
	converted = 'Value = {} converted into GB = {}'.format(value,gb)
	print(converted)
	
convert(2048)	