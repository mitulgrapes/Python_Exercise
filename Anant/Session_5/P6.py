import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="123",
 database="productdb"
)

mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE products (id bigint,name VARCHAR(255), price VARCHAR(255))")
#mycursor.execute("CREATE TABLE products_category (id bigint,product_id bigint,category_id bigint)")
#mycursor.execute("CREATE TABLE category (id bigint,name VARCHAR(255))")

mycursor.execute("SELECT * FROM products_category")
myresult = mycursor
print(myresult)



