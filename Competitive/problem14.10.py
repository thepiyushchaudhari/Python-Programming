Largest = lambda No1, No2, No3 : No1 if No1 > No2 and No1 > No3 else No2 if No2 > No3 else No3

def main ():
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    num3 = int(input("Enter third number :"))
    
    print("Largest Number is : ", Largest(num1,num2,num3))

if __name__ == "main" :
    main()