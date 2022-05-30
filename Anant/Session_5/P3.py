import json
# Use below json and display latest product on top:

product_string='[{"name":"Product-1","sku":"PROD-001","price":1550,"created_at":"2022-05-12 14:05:05"},{"name":"Product-2","sku":"PROD-002","price":2500,"created_at":"2022-05-23 10:00:01"},{"name":"Product-3","sku":"PROD-003","price":700,"created_at":"2022-04-12 07:00:00"},{"name":"Product-4","sku":"PROD-004","price":2150,"created_at":"2022-05-05 06:00:00"},	{"name":"Product-5","sku":"PROD-005","price":5000,"created_at":"2022-05-16 12:05:05"}]'

def extract_product(json):
    try:
        return str(json['created_at'])
    except KeyError:
        return 0

product_string.sort(key=extract_product, reverse=True)

