print("-------------------------------------------------")
print('3) Use below json and sort by price high to low:\
	\n[{"name":"Product-1","sku":"PROD-001","price":1550},{"name":"Product-2","sku":"PROD-002","price":2500},{"name":"Product-3","sku":"PROD-003","price":700},{"name":"Product-4","sku":"PROD-004","price":2150},{"name":"Product-5","sku":"PROD-005","price":5000}]')
print("-------------------------------------------------")

import json
import ast
jsondata = '[{"name":"Product-1","sku":"PROD-001","price":1550},{"name":"Product-2","sku":"PROD-002","price":2500},{"name":"Product-3","sku":"PROD-003","price":700},{"name":"Product-4","sku":"PROD-004","price":2150},{"name":"Product-5","sku":"PROD-005","price":5000}]'

my_dict = ast.literal_eval(jsondata)

def sort_price(json):
	return int(json['price'])
    
my_dict.sort(key=sort_price, reverse=True)
print(my_dict)