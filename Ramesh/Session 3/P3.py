# Print total odd & even number between 1 to 50

for num in range(1, 51):
    if num % 2 == 0:
        print("Even :" + num, end = " ")
    else:
        print("Odd :" + num, end = " ")
