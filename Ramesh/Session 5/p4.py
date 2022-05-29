# Demonstrate the use of multiple except statement

try:
    name = 'Bob'
    name += 5
except NameError as ne:
    # Code to handle NameError
    print(ne)
except TypeError as te:
    # Code to handle TypeError
    print(te)
