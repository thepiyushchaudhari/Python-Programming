'''
input : 123
output : 321

'''
def RevDigit (No):
    Rev = 0
    Digit = 0 
    while (No != 0):
        Digit = No % 10
        Rev = (Rev * 10) + Digit
        No = No // 10    
    return Rev 

def main():
    num = int(input("Enter a number :"))  
    Ret = RevDigit(num)
    print(Ret)

if __name__ == "__main__":
    main ()
