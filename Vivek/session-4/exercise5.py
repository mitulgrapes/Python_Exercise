print("-------------------------------------------------")
print(" 5) Print current date time. Format: 2022-05-16 06:09:38 AM ")
print("-------------------------------------------------")
import datetime

x = datetime.datetime.now()

print(x.strftime("%Y-%m-%d %H:%I:%S %p "))