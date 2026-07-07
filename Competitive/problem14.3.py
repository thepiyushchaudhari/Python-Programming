MaxNum = lambda No1, No2 : No1 if No1 > No2 else No2 
def main ():
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    
    print(MaxNum(num1,num2))
    
if __name__ == "__main__" :
    main ()
    