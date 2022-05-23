
import datetime

print(
    "1) Create class with one method to print firstname, lastname & email with use of self parameter \n")


class Personal:
    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email


obj = Personal("Anil", "Prajapati", "anil@grapesssolution.com")
display = 'FirstName = {}\nLastName = {}\nEMail = {} '.format(
    obj.firstname, obj.lastname, obj.email)
print(display)


print("\n 2) Create parent class with method which convert minutes to seconds. Inherit this parent class in child class & call parent class method using child class to print seconds \n")


class PClass:
    def __init__(self, mins):
        self.mins = mins

    def Convert_Min_To_Secs(self):
        print("Total seconds = "+str(self.mins * 60))


class CClass(PClass):
    pass


obj = CClass(3)
obj.Convert_Min_To_Secs()


print("\n 3) Create class which print number from 1 to 10 using _iter_() & _next_() method \n")


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
        else:
            raise StopIteration

        return x


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

print("\n 4) Create module with dictionary and print each item value \n")
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

from Exercise2 import person1
print(person1["name"])
print(person1["age"])
print(person1["country"])


print("\n 5) Print current date time. Format: 2022-05-16 06:09:38 AM\n")


e = datetime.datetime.now()

print (e.strftime("%Y-%m-%d %H:%M:%S tt"))