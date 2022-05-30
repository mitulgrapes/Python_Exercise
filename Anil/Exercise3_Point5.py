import mysql.connector

mydb = mysql.connector.connect(
    host="167.86.120.153",
    user="harmonyusr",
    password="fVG#N!M@ppl@#",
    database="python_exercise"
)

mycursor = mydb.cursor()
#print("Insert product")
# sql = "INSERT INTO product (name,price) VALUES (%s, %s)"
# val = ("product1", "1000")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")


# print("update product")
# sql = "update product set price= 2000 where id=1"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected.")


# print("Insert category")
# sql = "INSERT INTO category (name) VALUES ('round')"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")


# print("update category")
# sql = "update category set name= 'princess' where name='round'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected.")

# print("Insert products_category")
# sql = "INSERT INTO products_category (product_id,category_id) VALUES (1,1)"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

print("Show records")
sql = "select p.name,GROUP_CONCAT(c.name) from products_category pc \
inner join product p on pc.product_id = p.id \
inner join category c on pc.category_id = c.id \
group by p.name"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)


