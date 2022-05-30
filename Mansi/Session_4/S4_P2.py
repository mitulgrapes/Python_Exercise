print("2) Create parent class with one method to pring name and inherit it in child class. Child class shouldn't contain body\n")

class Main:
	def __init__(self, fullname):    
		self.name = fullname 
		#self.lastname = lname
	def printname(self): 
		print(self.name)
		
class child(Main):
	pass
	
object = child("Mansi Satishkumar Patel")
object.printname()	

