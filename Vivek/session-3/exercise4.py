print(" 4) Check whether given alphabet is a vowel or consonant")
print("-------------------------------------------------")

strval = (input(" Please Enter String : "))
vcount = 0
ccount = 0
str = strval.lower();  
for i in range(0,len(str)):   
    #Checks whether a character is a vowel  
    if str[i] in ('a',"e","i","o","u"):  
        vcount = vcount + 1;  
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        ccount = ccount + 1;  

print("Total Vowel: " + format(vcount))
print("Total Consonant: " + format(ccount))
