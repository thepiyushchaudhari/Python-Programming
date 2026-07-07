from functools import reduce
CheckEven = lambda No : (No % 2 == 0)
Add = lambda No1, No2 : (No1 + No2)

def main():
    
    Data = [11,12,13,14,15,16,17,18,19,20]
    print("Input Data : ", Data)

    ReduceData = (reduce(Add, Data))
    print("Data after Reduction : ", ReduceData)
    
if __name__ == "__main__" :
    main()
    