from functools import reduce

Addition = lambda x1, x2 : x1 + x2

def main ():
    Value = int(input("Enter number of elements you want : "))
    AddLst = []

    for i in range(0,Value):
        element = int(input(f"Enter element {i + 1}: "))
        AddLst.append(element)
    
    print(AddLst)

    if AddLst :
        ReduceData = (reduce(Addition, AddLst))
        print("Addition of list is  : ", ReduceData)
    
    else:
        print("List is Empty")

if __name__ == "__main__" :
    main ()