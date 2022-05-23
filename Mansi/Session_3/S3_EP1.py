# Python Program to Convert seconds into hours, minutes and seconds
  
import time
  
def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(n))
      
# Driver program
n = 12346
print(convert(n))