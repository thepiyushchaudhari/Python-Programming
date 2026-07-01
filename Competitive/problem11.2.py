'''
input : 7521
output : 4

'''
def CountDigit (No):
    Count = 0
    Digit = 0 
    while (No != 0):
        Digit = (Digit % 10==0)
        No = No // 10
        Count = Count+1
          
    return Count

def main():
    num = int(input("Enter a number :"))  
    Ret = CountDigit(num)
    print(Ret)

if __name__ == "__main__":
    main ()
