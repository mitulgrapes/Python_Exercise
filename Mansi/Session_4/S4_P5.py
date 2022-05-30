print("5) Create a class with multiple properties & remove some properties.\n")

class Test:
	def __init__(self,fname,lname,fullname,age,gender,country,phone,hobby):
		self.fname = fname
		self.lname = lname
		self.fullname = fullname
		self.age = age
		self.gender = gender
		self.country = country 
		self.phone = phone
		self.hobby = hobby 
	
object = Test("Mansi","Patel","Mansi S Patel",24,"female","India",9925006276,"Music")

printvalue = ' FirstName = {} \n LastName = {} \n FullName = {} \n Age = {} \n Gender = {} \n Phone = {} \n hobby = {}'.format(object.fname,object.lname,object.fullname,object.age,object.gender,object.country,object.phone,object.hobby)

print(printvalue)

del object.fullname
del object.gender

printvalue = '\n FirstName = {} \n LastName = {} \n Age = {} \n Phone = {} \n hobby = {}'.format(object.fname,object.lname,object.age,object.country,object.phone,object.hobby)

print(printvalue)