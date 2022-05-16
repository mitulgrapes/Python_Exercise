#Create a function which takes milliseconds as parameter & convert it to minutes
def convertMillis(millis):
     minutes=(millis/(1000*60))%60
     print (minutes, end = " ")

convertMillis(1652623760851)
