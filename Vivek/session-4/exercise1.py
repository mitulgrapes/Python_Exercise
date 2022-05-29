print("-------------------------------------------------")
print(" 1) Create class with one method to print firstname, lastname & email with use of self parameter")
print("-------------------------------------------------")

class userdetails:
    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        pass


a = userdetails("Vivek", 'Acharya', "vivek.acharya@grapes-solutions.com")

print('First Name: '+a.firstname)
print("Last Name: "+a.lastname)
print("Email "+a.email)