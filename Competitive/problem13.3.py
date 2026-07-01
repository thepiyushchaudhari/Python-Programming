def perfectNum(Num):
    if Num <= 0:
        return False
        
    divisor_sum = 0
    
    for i in range(1, Num):
        if Num % i == 0:
            divisor_sum += i 
            
    return divisor_sum == Num
        
def main():
    num = int(input("Enter a number: "))  
    Ret = perfectNum(num)
    
    if Ret:
        print("Perfect number")
    else:
        print("Not a perfect number")

if __name__ == "__main__":
    main()
