#Demonstrate the use of try except statement with finally

def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("You are dividing by zero ")
    else:
        print("Your answer is :", result)
    finally: 
        print('This is always executed')  
 
divide(0, 1)
divide(1, 0)