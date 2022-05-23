from lib2to3.pytree import convert


class Converter :
    def __init__(self,seconds):
        self.seconds = seconds
        
    def printseconds(self):
        minutes = self.seconds * 60
        print(minutes)

class Receiver(Converter):
        
        def __init__(self, seconds):
            super().__init__(seconds)

Convert = Receiver(26)

Convert.printseconds()


