print(" 5) Create a function which takes 2 argument. First as list & second as index. So print value which is exist at given index")
print("-------------------------------------------------")

def function_index_val(listval, index):

    print('index  '+format(index)+' '+ listval[index])   


listval = ['Mango','Watermelon','Apple','Orange','Guava','Grapes']
function_index_val(listval, 0)
function_index_val(listval, 1)
function_index_val(listval, 2)
function_index_val(listval, 3)
function_index_val(listval, 4)
