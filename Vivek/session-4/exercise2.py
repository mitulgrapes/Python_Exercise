print("-------------------------------------------------")
print(" Create parent class with method which convert minutes to seconds. Inherit this parent class in child class & \
    call parent class method using child class to print seconds")
print("-------------------------------------------------")

class parentclass:

    def __init__(self,minute):
        self.minute = minute

    def minute_to_second(self):
         dis_second =((self.minute)*60)
         print("Convert minute: "+format(self.minute)+" to Second: "+format(dis_second))

class childclass(parentclass):
    pass

parent_obj = childclass(15)
parent_obj.minute_to_second()