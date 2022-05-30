import json


test_str =  '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'

data = json.loads(test_str)

for k1, v1 in data.items():
    print(k1 + ': '+ v1)