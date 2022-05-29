print("-------------------------------------------------")
print(" Create class which print number from 1 to 10 using _iter_() & _next_() method")
print("-------------------------------------------------")

class parentclass:

    def __iter__(self):
        self.start = 1
        return self
    def __next__(self):
        nextval = self.start
        self.start += 1
        return nextval
    

parent_obj = parentclass()
myiter = iter(parent_obj);

print(next(myiter));
print(next(myiter));
print(next(myiter));
print(next(myiter));
print(next(myiter));
print(next(myiter));
print(next(myiter));
print(next(myiter));
print(next(myiter));
print(next(myiter));

