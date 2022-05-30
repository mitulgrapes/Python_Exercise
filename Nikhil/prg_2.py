import json

data = {
    "name": "jane doe",
    "salary": 9000,
    "email": "JaneDoe@pynative.com"
}

result = json.dumps(data, indent=5, separators=(", ", ": "))
print(result)