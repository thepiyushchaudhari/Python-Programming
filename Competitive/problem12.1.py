'''
input : a
output : Given Alphabet is a Vowel

'''
def CheckVowel (Char):
    if(Char in 'aeiouAEIOU'):
        return True
    else:
        return False

def main():
    Char = (input("Enter a Alphabet :"))  
    Ret = CheckVowel(Char)
    
    if(Ret == True):
        print("Given Alphabet is a Vowel")
    else:
        print("Given Alphabet is Not a Vowel")

if __name__ == "__main__":
    main ()
