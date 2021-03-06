"""
Use below json and display latest product on top:
  [{"name":"Product-1","sku":"PROD-001","price":1550,"created_at":"2022-05-12 14:05:05"},
  {"name":"Product-2","sku":"PROD-002","price":2500,"created_at":"2022-05-23 10:00:01"},
  {"name":"Product-3","sku":"PROD-003","price":700,"created_at":"2022-04-12 14:05:05"},
  {"name":"Product-4","sku":"PROD-004","price":2150,"created_at":"2022-05-05 06:00:00"},
  {"name":"Product-5","sku":"PROD-005","price":5000,"created_at":"2022-05-16 12:05:05"}]
"""

print("Use below json and display latest product on top. \n")

import json 

example =  '[{"name":"Product-1","sku":"PROD-001","price":1550,"created_at":"2022-05-12 14:05:05"},{"name":"Product-2","sku":"PROD-002","price":2500,"created_at":"2022-05-23 10:00:01"},{"name":"Product-3","sku":"PROD-003","price":700,"created_at":"2022-04-12 14:05:05"},{"name":"Product-4","sku":"PROD-004","price":2150,"created_at":"2022-05-05 06:00:00"},{"name":"Product-5","sku":"PROD-005","price":5000,"created_at":"2022-05-16 12:05:05"}]'
			
print(example)		

convert = json.loads(example)	

check = json.dumps(convert, indent=3, sort_keys=True)

print(check)

