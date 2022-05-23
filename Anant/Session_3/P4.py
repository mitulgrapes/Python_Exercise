#Find the price range in which given price is match. Take price = 7999
#Price Range: 1000 to 5000, 5001 to 10000, 10001 to 15000

Price_range_1 = range(1000, 5000)
Price_range_2 = range(5001, 10000)
Price_range_3 = range(10001, 15000)
number = int(input('Enter a number : '))
 
if number in Price_range_1 :
    print(number, 'is present in the Price_range_1.')
elif number in Price_range_2:
    print(number, 'is not present in the Price_range_2.')
else:
    print(number, 'is not present in the Price_range_3.')
