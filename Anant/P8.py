DataList = {
    'Firstname': 'Anant',
    'Lastname': 'Patel',
    'Age': 26,
    'ContactNo': 1234567890,
}

print(DataList)

DataList['Address'] = 'Kalol'
print(DataList)

DataList.pop('Age')
print(DataList)
