def PrintNums (Num1, Num2):
    print(Num1 + Num2)
    print(Num1 - Num2)
    print(Num1 * Num2)
    print(Num1 / Num2)
        
def main():
    num1 = int(input("Enter 1st number :"))  
    num2 = int(input("Enter 2nd number :")) 
    PrintNums(num1, num2)
   

if __name__ == "__main__":
    main ()