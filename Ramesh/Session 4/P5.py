# Create a class with multiple properties & remove some properties

class UserData:
    def __init__(self, name, age, phone, countryname):
        self.name = name
        self.age = age
        self.phone = phone
        self.countryname = countryname
        pass


a = UserData("Ramesh", 26, '8855220066', "India")
del a.country
print(a.name)
print(a.age)
print(a.country)
