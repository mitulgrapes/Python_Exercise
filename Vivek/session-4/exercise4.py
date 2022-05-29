print("-------------------------------------------------")
print(" 4) Create module with dictionary and print each item value ")
print("-------------------------------------------------")
import exercise4_module #for call method
from exercise4_module import get_user

print(get_user['name'])
print(get_user['mobile'])
exercise4_module.persondata('Vivek Acharya') 