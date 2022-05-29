# Print any json to readable format with 5 indent & ,(comma) as separator

import json

# Initialize JSON data
json_data = '[ {"studentid": 1, "name": "ABC", "subjects": ["Python", "Data Structures"]}, \
                {"studentid": 2, "name": "PQR", "subjects": ["Java", "Operating System"]} ]'

# Create Python object from JSON string data
obj = json.loads(json_data)

# Pretty Print JSON
json_formatted_str = json.dumps(obj, indent=5,',')
print(json_formatted_str)
