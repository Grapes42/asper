class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

word = input("Enter Word: ")

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

extendable = "m"

pos = 0
met_vow = False
met_cons = True

i = 0

while i < len(word):
    if word[i] in vowels and met_vow:
        pos = i

        if word[i-1].lower() in extendable:
            pos += 1
        
        break

    if word[i] in vowels:
        met_vow = True
    
    i += 1

print(color.BOLD + word[: pos] + color.END + word[pos :])