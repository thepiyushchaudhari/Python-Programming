'''
input : 123
output : 6

'''
def SumDigits (No):
    Count = 0
    Digit = 0 
    while (No != 0):
        Digit = No % 10
        No = No // 10
        Count = Count + Digit    
    return Count

def main():
    num = int(input("Enter a number :"))  
    Ret = SumDigits(num)
    print(Ret)

if __name__ == "__main__":
    main ()
