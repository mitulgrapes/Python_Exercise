print(" 6) Create a function which takes milliseconds as parameter & convert it to minutes")
print("-------------------------------------------------")

millisecond=input("Enter time in milliseconds ")
millis = int(millisecond)
seconds=(millis/1000)%60
seconds = int(seconds)
minutes=(millis/(1000*60))%60
minutes = int(minutes)
hours=(millis/(1000*60*60))%24

print ("%d Hour:%d Minute:%d Second" % (hours, minutes, seconds))