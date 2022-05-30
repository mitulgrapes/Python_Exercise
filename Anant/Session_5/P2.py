# Format below json
#sampleJson = {"key1": "value1", "key2": "value2"}
import json

a = {"Firstname": "Anant", "Age": 27, "City": "Kalol", "Contact": "0123456789"}
b = json.dumps(a)
print(b)
