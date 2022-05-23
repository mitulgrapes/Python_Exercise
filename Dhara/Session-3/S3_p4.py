range_1 = range(1000, 5000)
range_2 = range(5001, 10000)
range_3 = range(10001, 15000)
val = 7999
 
if val in range_1 :
    print(val, 'Enter value is in range 1.')
elif val in range_2:
    print(val, 'Enter Value is in range 2.')
else:
    print(val, 'Enter Value is in range 3.')
