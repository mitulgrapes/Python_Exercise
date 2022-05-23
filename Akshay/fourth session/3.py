class Iteration:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1

a = 1
b = 10

c = Iteration(a,b)

for i in c:
    print(1)

