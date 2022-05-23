print("5) Create a function which takes 2 argument. First as list & second as index. So print value which is exist at given index\n")

def my_function(list,x):
  print("The powerful country  is " + list[x])
  
x = int(input("Enter a value index \n"))   
list=["USA","UK","India","Japan","Canada","Russia","Australia"]
my_function(list,x)