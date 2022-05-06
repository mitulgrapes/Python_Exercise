# 6) Create tuple with 5 items & add other 2 new items and then print all items
tup = ('a','b','new','d','e')
lis = list(tup)
lis[2] = 'c'
lis.append ('Append New')
tup = lis
#print(type(t))
print(tup)