from math import degrees
from msilib.schema import ListView
from socket import herror

print("1) Store your personal information in variables and print it. (Fields: Firstname, Lastname, Email, Contact No, Age, Height\n")

Firstname = "Anil"
Lastname = "Prajapati"
Email = "anil@grapessolution.com"
ContactNo = "9898171013"
Age = 31
Height = "5'6''"
#print("FirstName = "+Firstname+"\nLastName = "+Lastname+"\nEMail = "+Email+"\nContactNo = "+ContactNo+"\nAge = "+str(Age)+"\nHeight = "+Height)
PersonalInfo = 'FirstName = {}\nLastName = {}\nEMail = {} \nContactNo = {}\nAge = {}\nHeight = {}'.format(Firstname,Lastname,Email,ContactNo,Age,Height)
print(PersonalInfo)
print("\n")


print("2) Create four variables with different type and print its data type\n")
Firstname = "Anil"
Age = 31
Hobbies =  ["Cricket", "Dancing"]
Degrees = ("BCA", "MCA")

ShowTypeOfVariable = 'Firstname is of type ={}\nAge is of type ={}\nHobbies is of type ={}\nDegrees is of type ={}'.format(type(Firstname),type(Age),type(Hobbies),type(Degrees))
print(ShowTypeOfVariable)
print("\n")


print("3) Declare a list with 4 items. Add new item at 2nd position then change value of 4th item and print whole list\n")
ListVar =  ["India", "USA", "UK", "AUS"]
print("List with 4 items ")
print(*ListVar, sep = "\n")

ListVar.insert(1,"New Zealand")
print("\nAdded new item at 2nd position ")
print(*ListVar, sep = "\n")


ListVar[3]="Canada"
print("\nChange value of 4th item ")
print(*ListVar, sep = "\n")

print("\n")
print("4) Create a list of country name and make copy of this list & then print new copied list\n")
NewList = ListVar.copy()
print(*NewList, sep = "\n")


print("\n")
print("5) Create tuple with 10 items & print it\n")
TupleVar = ("Wordpress",".Net", "PHP", "Laravel","Magento","Shopify","Angular","React","NodeJS","Android","iOS")
print(*TupleVar, sep = "\n")


print("\n")
print("6) Create tuple with 5 items and print 3rd & 5th item value\n")
TupleVar = ("Wordpress",".Net", "PHP", "Laravel","Magento")
print("3rd item = "+TupleVar[2] +"\n5th item = "+TupleVar[4])


print("\n")
print("7) Create set with 3 items and remove & add any item\n")
SetVar = {"Ahmedabad", "Surat", "Rajkot"}
print("Set with 3 items")
print(*SetVar, sep = "\n")
print("\nAdded new item")
SetVar.add("Vadodara")
print(*SetVar, sep = "\n")
print("\nRemove any item")
SetVar.remove("Vadodara")
print(*SetVar, sep = "\n")



print("\n")
print("8) Create dictionary with any items. Add new item & remove existing item.\n")
DictionaryVar = {
    'name': 'Anil Prajapati',
    'height': '5.6ft',
    'salary': 2000
}
print(DictionaryVar)
print("\nAdded new item")
DictionaryVar["ExpectedSalary"] = 2500
print(DictionaryVar)

print("\nRemove any item")
DictionaryVar.pop("ExpectedSalary")
print(DictionaryVar)

