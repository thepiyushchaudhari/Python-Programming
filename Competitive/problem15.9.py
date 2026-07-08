from functools import reduce

Product = lambda x1, x2 : x1 * x2 

def main():
    Data = [11,12,13,14,15,16,17,18,19,20]
    print("Input Data : ", Data)

    ReduceData = (reduce(Product, Data))
    print("Data after Reduction : ", ReduceData)
    
if __name__ == "__main__" :
    main()
    