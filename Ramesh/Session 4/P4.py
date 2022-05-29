# Create module which convert MB to GB

try:
    mb = int(input("Enter MB:- "))
    convert = mb / 1024
    print(convert," GB")
except ValueError:
    pass
    

