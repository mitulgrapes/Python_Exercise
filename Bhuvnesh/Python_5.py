# json convert into python dictionary
import json
import mysql.connector
json_obj = '{"Name": "Bhuvneh","RollNo": "2526"}'
data = json.loads(json_obj)
print(data)
print("Rollno:" + data["RollNo"])

# Print json to readable format
datastr = {
    "Name": "John cena",
    "Age": 50,
    "Country": "USA"
}
datajson = json.dumps(datastr, indent=5)
print(datajson)

# sort by price high to low:
products = [{"name": "Product-1", "sku": "PROD-001", "price": 1550},
            {"name": "Product-2", "sku": "PROD-002", "price": 2500},
            {"name": "Product-3", "sku": "PROD-003", "price": 700},
            {"name": "Product-4", "sku": "PROD-004", "price": 2150},
            {"name": "Product-5", "sku": "PROD-005", "price": 5000}
            ]
newlst = sorted(products, key=lambda x: x["price"], reverse=True)
print(newlst)
# except

a, b = 10, 'a'
try:
    print(a/b)
    print("This won't be printed")
except TypeError:
    print("You added values of incompatible types")
except ZeroDivisionError:
    print("You divided by 0")

#string using format() method.
first_name = "Bhuvnesh"
last_name = "Mishra"
email = 'bhuvnesh.mishra@grapes-solutions.com'
contact_no = 7791964181
age = 27
height = 5.10
personal_information = "Name: {} {}\nEmail:{}\nContact No: {}\nAge: {}\nHeight: {}".format(
    first_name, last_name, email, contact_no, age, height)
print(personal_information)
#db connection
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='PythonProj',
                                         user='bhuvnesh',
                                         password='8890519507@Bm')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")