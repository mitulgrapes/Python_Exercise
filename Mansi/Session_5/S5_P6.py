"""
6) Create three tables: products and products_category. Insert, update
records and display products with category name. If product have
multiple category then show category comma separatd. Must add multiple
category in some product
     products table columns:
     id, name, price,

     category table columns:
     id, name

     products_category table columns:
     id,product_id,category_id
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="mansi",
  password="grapes@123"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE testdatabase")

mydb = mysql.connector.connect(
  host="localhost",
  user="mansi",
  password="grapes@123",
  database="testdatabase"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE products (name VARCHAR(255), price VARCHAR(255))")
mycursor.execute("CREATE TABLE category (name VARCHAR(255))")
mycursor.execute("CREATE TABLE products_category (product_id int,category_id int)")

sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
val = ("Ring1", "2000")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
val = [
  ('DiamondRing2', '1200'),
  ('Earrings3', '1500'),
  ('Necklace4','2500'),
  ('Band5','3000'),
  ('Band6','3300')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

sql = "INSERT INTO category (name) VALUES (%s)"
val = [
  ('Ring'),
  ('Earrings'),
  ('Necklace'),
  ('Band'),
  ('Set')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

sql = "INSERT INTO products_category (product_id, category_id) VALUES (%s, %s)"
val = [
  ('DiamondRing2', '1200'),
  ('Earrings3', '1500'),
  ('Necklace4','2500'),
  ('Band5','3000'),
  ('Band6','3300')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")



