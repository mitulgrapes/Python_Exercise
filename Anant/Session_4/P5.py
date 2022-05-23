# Create a class with multiple properties & remove some properties

class UserData:
    def __init__(self, name, age, contactno, country):
        self.name = name
        self.age = age
        self.contactno = contactno
        self.country = country
        pass


a = UserData("Anant", 26, '012345678', "India")
del a.country
print(a.name)
print(a.age)
print(a.country)
