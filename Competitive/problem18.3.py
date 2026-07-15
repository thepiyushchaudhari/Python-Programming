from functools import reduce

Min = lambda x1, x2 : x1 if x1 < x2 else x2

def main ():
    Value = int(input("Enter number of elements you want : "))
    Lst = []

    for i in range(0,Value):
        element = int(input(f"Enter element {i + 1}: "))
        Lst.append(element)
    
    print(Lst)

    if Lst :
        ReduceData = (reduce(Min,Lst))
        print("Minimum value is  : ", ReduceData)
    
    else:
        print("List is Empty")

if __name__ == "__main__" :
    main ()