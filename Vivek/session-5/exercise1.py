print("-------------------------------------------------")
print(" 1) Use any json string & convert it into python dictionary and print each key and value. (Ex, Name: Abc, Roll No: 1)")
print("-------------------------------------------------")
import json
x = '{"roll_no":"1","name":"Vivek Acharya","email":"vivek.acharya@grapes-solutions.com"}'

y = json.loads(x)

for key in y:
    print(key, ":", y[key])

# print('Roll NO: '+y['roll_no'])
# print('Name: '+y['name'])
# print('Email: '+y['email'])
