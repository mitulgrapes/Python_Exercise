import mysql.connector

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password= "")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price INT")
mycursor.execute("CREATE TABLE category (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255)")
mycursor.execute("CREATE TABLE products_category (product_id INT, category_id INT")

sql = "INSERT INTO products (name, price) VALUES (%s, %d)"
val = [
  ('prodd_1', 100),
  ('prodd_2', 200),
  ('prodd_3', 300)
]

mycursor.executemany(sql, val)

mydb.commit()

sql = "INSERT INTO category (name) VALUES (%s)"
val = [
  ('categ_1'),
  ('categ_2'),
  ('categ_3')
]

mycursor.executemany(sql, val)

mydb.commit()

sql = "UPDATE products SET price = 250 WHERE name = 'prodd_3'"

mycursor.execute(sql)

mydb.commit()