print("4) Check whether given alphabet is a vowel or consonant\n")

ch = str(input("Enter Any Alphabet: "))

if ch.lower() in ('a', 'e', 'i', 'o', 'u'):

  print("Vowel")

elif ch.upper() in ('A', 'E', 'I', 'O', 'U'):

  print("Vowel")

else:

  print("Consonant")
