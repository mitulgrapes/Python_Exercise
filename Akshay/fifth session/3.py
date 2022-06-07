#3) Use below json and sort by price high to low:
#	[{"name":"Product-1","sku":"PROD-001","price":1550},{"name":"Product-2","sku":"PROD-002","price":2500},{"name":"Product-3","sku":"PROD-003","price":700},{"name":"Product-4","sku":"PROD-004","price":2150},{"name":"Product-5","sku":"PROD-005","price":5000}]


import json
products = [{"name":"Product-1","sku":"PROD-001","price":1550},{"name":"Product-2","sku":"PROD-002","price":2500},{"name":"Product-3","sku":"PROD-003","price":700},{"name":"Product-4","sku":"PROD-004","price":2150},{"name":"Product-5","sku":"PROD-005","price":5000}]

ascending = sorted(products,key = lambda d : d['price'],reverse= True)
# ascending  = json.dumps(products, indent=3, sort_keys=True)

print(ascending)