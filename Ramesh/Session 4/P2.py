#Create parent class with one method to pring name and inherit it in child class.
#Child class shouldn't contain body

class Main:
	def __init__(self, data):
		self.data = data
	def printname(self):
		print(self.data)

class child(Main):
	pass

object = child("Abcdef")
object.printname()	
