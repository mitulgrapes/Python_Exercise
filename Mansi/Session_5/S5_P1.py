print("1) Use any json with multiple rows and search specific value from json.\n")

import json

a = '{"std":"12", "stream":"Science", "subject":"Maths", "Board":"GHSEB" , "Year":2022, "Course":"Engineering"}'

convert = json.loads(a)

print(convert["subject"])