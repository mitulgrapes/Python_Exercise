# Use any json string & convert it into python dictionary and print each key and value. (Ex, Name: Abc, Roll No: 1)

json_string = '{ "name":"Jack", "age":21, "city":"California"}'

json_dictionary = json.loads(json_string)

for key in json_dictionary:
    print(key, ":", json_dictionary[key])
