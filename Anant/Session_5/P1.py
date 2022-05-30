import json

# Use any json with multiple rows and search specific value from json

a = '{"Firstname":"Anant","Age":26,"City":"Kalol","Contact":"0123456789"}'
b = json.loads(a)
print(b["Firstname"])
