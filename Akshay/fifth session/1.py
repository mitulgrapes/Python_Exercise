import json

#1) Use any json string & convert it into python dictionary and print each key and value. (Ex, Name: Abc, Roll No: 1)
person = '{"name": "Bob", "languages": ["English", "French"],"Roll No" : "1"}'
person_dict = json.loads(person)

print(person_dict)