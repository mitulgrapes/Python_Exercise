# 4) Find the price range in which given price is match. Take price = 7999
# 	Price Range: 1000 to 5000, 5001 to 10000, 10001 to 15000

number = 7999

for i in range(1000,5000):
    if i == number:
        print(number, "is between 1000 , 5000")
   # 4) Find the price range in which given price is match. Take price = 7999
# 	Price Range: 1000 to 5000, 5001 to 10000, 10001 to 15000

number = 7999

for i in range(1000,5000):
    if i == number:
        print(number, "is between 1000 , 5000")
    else:
        pass
for i in range(5001,10000):
    if i == number:
        print(number, "is between 5001,10000")
    else:
        pass
for i in range(10001,15000):
    if i == number:
        print(number, "is between 10001 , 15000")
    else:
        pass
