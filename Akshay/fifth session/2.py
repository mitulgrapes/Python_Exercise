#2) Print any json to readable format with 5 indent & ,(comma) as separator
import json

x = '[{"roll_no":"1", "name":"Vivek"},{"roll_no":"2", "name":"Chintan"},{"roll_no":"3", "name":"Amit"}]' 

obj = json.loads(x)
# print(obj)
y = json.dumps(obj, indent=5,separators=(',',':'))

print(y)