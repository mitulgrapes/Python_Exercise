print("-------------------------------------------------")
print('Create three tables: products and products_category. Insert, update records and display products with category name \
	products table columns:\
	id, name, price\
	category table columns:\
	id, name\
	products_category table columns:\
	id,product_id,category_id')
print("-------------------------------------------------")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Grapes@123",
  database="python_session"
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)


# mycursor.execute("CREATE DATABASE python_session")

mycursor.execute("CREATE TABLE products (id INT(11), name VARCHAR(255), price VARCHAR(11))")

mycursor.execute("CREATE TABLE category (id INT(11), name VARCHAR(255))")

mycursor.execute("CREATE TABLE product_category (id INT(11), product_id INT(11), category_id INT(11))")

sql = "INSERT INTO products (id, name, price) VALUES (%s, %s, %s)"
val = (1, "Eternity Ring", '15000')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO category (id, name) VALUES (%s, %s)"
val = (1, "Ring")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO product_category (id, product_id, category_id) VALUES (%s, %s, %s)"
val = (1, 1, 1)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

sql = "UPDATE products SET name = %s WHERE id = 1"
val = [("Men Ring")]
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record updated.")

mycursor.execute("SELECT products.name, category.name FROM product_category join products on products.id = product_category.product_id join category on category.id = product_category.category_id where product_category.id = 1")

res = mycursor.fetchall()

for x in res:
  print(x)
