# print number using while loop
num = 1
while(num <= 10):
    print(num)
    num += 1

# pattern


def numpattern(n):
    numpet = 1
    for i in range(0, n):
        numpet = 1
        for j in range(0, i+1):
            print(numpet, end=" ")
            numpet = numpet + 1
        print("\r")


n = 5
numpattern(n)
# Print odd & even number using while loop
num = 50
number = 1
while number <= num:
    if(number % 2 != 0):
        print("ODD:" + str(number))
    else:
        print("Even:" + str(number))
    number = number + 1
#
val = input("Please Enter Your Own Character : ")

if(val == 'A' or val == 'a' or val == 'E' or val == 'e' or val == 'I'
   or val == 'i' or val == 'O' or val == 'o' or val == 'U' or val == 'u'):
    print(val, "is a Vowel")
else:
    print(val, "is a Consonant")

#


def get_index_value(_list, _index):
    if len(_list) >= _index:
        print(_list[_index])
    else:
        print("Invalid index.")


list_ele = ["fname", "lname", "email"]
index_val = 2
get_index_value(list_ele, index_val)

# milliseconds convert it to minutes
millis = input("Enter time in milliseconds ")
millis = int(millis)
minutes = (millis/(1000*60)) % 60
minutes = int(minutes)

print("%d" % (minutes))

