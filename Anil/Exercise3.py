from cmath import log
import json

print('1) Use any json with multiple rows and search specific value from json\n')

x = [{
    "name": "John",
    "age": 30,
    "city": "New York"
},
    {
    "name": "John abraham",
    "age": 30,
    "city": "New York"
}, {
    "name": "Shakti",
    "age": 30,
    "city": "New York"
}]

data = json.loads(json.dumps(x))
seachInput = input("Enter a search keyword: \n")
for item in x:
    # print(item)
    if seachInput in item:
        print("The value of", seachInput, "is", item)
#
# if seachInput in data:
#     print("The value of", seachInput, "is", data[seachInput])
# else:
#     print("Search value not found")

print('\n 2) Format below json')
print('\nsampleJson = {"key1": "value1", "key2": "value2"}')

x = {"key1": "value1", "key2": "value2"}
y = json.dumps(x, indent=4, separators=(", ", " = "))
print(y)

print("\n 3) Use below json and display latest product on top")
data = [{"name": "Product-1", "sku": "PROD-001", "price": 1550, "created_at": "2022-05-12 14:05:05"},
        {"name": "Product-2", "sku": "PROD-002", "price": 2500,
            "created_at": "2022-05-23 10:00:01"},
        {"name": "Product-3", "sku": "PROD-003", "price": 700,
            "created_at": "2022-04-12 14:05:05"},
        {"name": "Product-4", "sku": "PROD-004", "price": 2150,
            "created_at": "2022-05-05 06:00:00"},
        {"name": "Product-5", "sku": "PROD-005", "price": 5000, "created_at": "2022-05-16 12:05:05"}]

data.sort(key=lambda x: x["created_at"])
print(data)

print("\n 4) Demonstrate the use of try except statement with finally")
try:
    result = 10/0
except:
    print("exception throws")
finally:
    print("The 'try except' is finished")


print("\n 5) Add varible value in string using format() method.")

Firstname = "Anil"
Lastname = "Prajapati"
Email = "anil@grapessolution.com"
ContactNo = "9898171013"
Age = 31
Height = "5'6''"
PersonalInfo = 'FirstName = {}\nLastName = {}\nEMail = {} \nContactNo = {}\nAge = {}\nHeight = {}'.format(Firstname,Lastname,Email,ContactNo,Age,Height)
print(PersonalInfo)

print(" 5)  Create three tables: products and products_category. Insert, update records and display products with category name. If product have multiple category then show category comma separatd. Must add multiple category in some product")
# please refer file Exercise3_Point5