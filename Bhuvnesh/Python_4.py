#
from datetime import datetime


class WWE:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.age = age
        self.lname = lname


p1 = WWE("John", "Cena", '50')
print("name:" + p1.fname + p1.lname + ' ' + 'age:' + p1.age)

# parent class with properties & method and inherit these properties & method in child class


class school:
    def __init__(self, name, lname):
        self.name = name
        self.lname = lname

    def printname(self):
        print(self.name, self.lname)


class Student(school):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.name, self.lname,
              "to the class of", self.graduationyear)


x = Student("John", "Cena", 1999)
x.welcome()

# tuple print each item using iter() & next() method
my_tuple = (1, 2, 3, 4, 5)
print(iter(my_tuple))
iter_obj = iter(my_tuple)
while True:
    try:

        element = next(iter_obj)
        print(element)

    except StopIteration:

        break

# compound interest using function


def compoundInterest(p, r, t):
    ci = p * (pow((1 + r / 100), t))
    return ci


p = float(input("Enter the principal amount : "))

t = float(input("Enter the number of years : "))

r = float(input("Enter the rate of interest : "))

ci = compoundInterest(p, r, t)

print("Compound interest : {}".format(ci))

# date time

# today = datetime.date.today()
new_year = datetime.strptime("16-5-2022 10:09:56 AM", "%d-%m-%Y %I:%M:%S %p").strftime("%d %b, %Y %I:%M:%S %p")
print(new_year)
