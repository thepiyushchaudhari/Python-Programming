'''
input : 121
output : Palindrome

'''
def RevDigit (No):
    Digit = 0 
    Rev = 0
    No1 = No

    while (No != 0):
        Digit = No % 10
        Rev = (Rev * 10) + Digit
        No = No // 10    
   
    if (Rev == No1):
        return True
    else:
        return False
        

def main():
    num = int(input("Enter a number :"))  
    Ret = RevDigit(num)
    
    if(Ret == True):
        print("Palindrome Number")
    else:
        print("Not a Palindrome")

if __name__ == "__main__":
    main ()
