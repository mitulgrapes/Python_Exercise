import datetime
# assign variables and print..
first_name = "Bhuvnesh"
last_name = "Mishra"
email = 'bhuvnesh.mishra@grapes-solutions.com'
contact_no = 7791964181
age = 27
height = 5.10
print(first_name + ' ' + last_name + ' ' + email + ' ' + ' ' +
      str(contact_no) + ' ' + str(age) + ' ' + str(height))

# Print variable using formate method

personal_information = "Name: {} {}\nEmail:{}\nContact No: {}\nAge: {}\nHeight: {}".format(
    first_name, last_name, email, contact_no, age, height
)
print(personal_information)

# variables with different data type
Is_boolean = True
print(type(first_name))
print((type(age)))
print(type(height))
print(type(Is_boolean))

# Declearing a list
States = ['Gujarat', 'Maharashtra', 'Rajasthan', 'Goa', 'Madhya Pradesh']
personal_info = [first_name, email, contact_no]
if "Gujarat" in States:
    print("Yes, 'Gujarat' is in the list")
 # Merge list
print(States + personal_info)
States.extend(personal_info)
print(States)

# tuple
technologies = ('HyperAutomation', 'Cybersecurity', 'Full Stack Development',
                'Blockchain', 'Edge Computing', 'Devops', 'AI', 'Blockchain', 'AWS', 'Data Science')
States_new = ('Gujarat', 'Maharashtra', 'Rajasthan')
print(technologies)
print(States_new.index('Rajasthan'))

# Create Set
Set_value = {'AI', 'Blockchain', 'AWS'}
Set_value.add('Cybersecurity')
Set_value.remove("Cybersecurity")
print(Set_value)

# Dictionaries

Infomations = {
    'Technology': 'Angular',
    'category': 'framework',
    'price': 0
}
print(Infomations)
