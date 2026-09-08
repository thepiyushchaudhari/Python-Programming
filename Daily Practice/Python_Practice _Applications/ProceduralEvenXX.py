def CheckEven (No):
    return (No % 2 == 0)

def main() :
    Value = int(input("Enter Number :"))
    Ret = CheckEven(Value)
    
    if(Ret == True):
        print("It's Even Number")
    
    else:
        print("It's Odd Number")
  
if __name__ == "__main__":
    main()
