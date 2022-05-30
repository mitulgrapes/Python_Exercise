"""
2) Format below json
     sampleJson = {"key1": "value1", "key2": "value2"}

    Output:
     {
       "key1" = "value2",
       "key2" = "value2",
       "key3" = "value3"
     } 
"""	 
import json 	 
	 
print("2) Format json. \n")

samplejson = '{"std":"12", "stream":"Science", "subject":"Maths", "Board":"GHSEB" , "Year":2022, "Course":"Engineering"}'

a = json.loads(samplejson)

#print(a)

formated = json.dumps(a, indent=2, separators=(",", " = "))

print(formated)

another = json.dumps(a, indent=4, sort_keys=True)

print(another)
