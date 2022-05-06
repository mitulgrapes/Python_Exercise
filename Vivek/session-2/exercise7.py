# 7) Create set with 3 items and remove & add any item
city = {"Ahmedabad",'Surat','Mumbai'}
city.add('pune')
print(city)
city.remove('Mumbai')
print(city)
city.discard('Vapi') #Not display error
print(city)