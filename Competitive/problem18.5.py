from functools import reduce

Addition = lambda x1, x2 : x1 + x2

def ChkPrime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False 
    return True  

def main():
    Value = int(input("Enter number of elements you want : "))
    AddLst = []

    for i in range(0, Value):
        element = int(input(f"Enter element {i + 1}: "))
        AddLst.append(element)
    
    print("Your input list:", AddLst)
    
    PrimeLst = [num for num in AddLst if ChkPrime(num)]
    print("Prime numbers found:", PrimeLst)

    if PrimeLst:
        ReduceData = reduce(Addition, PrimeLst)
        print("Addition of prime numbers is : ", ReduceData)
    else:
        print("No prime numbers were entered.")

if __name__ == "__main__":
    main()
