print("4) Demonstrate the use of try except statement with finally. \n")

try:
  a = {"std":"12", "stream":"Science", "subject":"Maths", "Board":"GHSEB" , "Year":2022, "Course":"Engineering"}
  convert = json.loads(a)
  print(a)
except:
  print("Something went wrong")
finally:
  print("Finally block is print")

