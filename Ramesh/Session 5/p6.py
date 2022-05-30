 # Create three tables: products and products_category. Insert, update records and display products with category name

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE python_excercize")

mycursor.execute("CREATE TABLE products (id INT(11), name VARCHAR(255), price INT(11))")

mycursor.execute("CREATE TABLE category (id INT(11), name VARCHAR(255))")

mycursor.execute("CREATE TABLE product_category (id INT(11), product_id INT(11), category_id INT(11))")

sql = "INSERT INTO products (id, name, address) VALUES (%d, %s, %d)"
val = (1, "Apple", 1500)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO category (id, name) VALUES (%d, %s)"
val = (1, "Fruit")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO product_category (id, product_id, category_id) VALUES (%d, %d, %d)"
val = (1, 1, 1)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

sql = "UPDATE products SET name = %s WHERE id = 1"
val = ("Banana")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record updated.")

mycursor.execute("SELECT products.name, category.name FROM product_category join products on products.id = product_category.product_id join category on category.id = product_category.category_id where product_category.id = 1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
