def main ():
    Value = int(input("Enter number of elements you want : "))
    Lst = []

    for i in range(0,Value):
        element = int(input(f"Enter element {i + 1}: "))
        Lst.append(element)
    
    print(Lst)

    NumFreq = int(input("Enter the number you want to count the frequency of : "))
    Ret = Lst.count(NumFreq)

    if Lst :
        print("Count of given number is   : ", Ret)
    
    else:
        print("List is Empty")

if __name__ == "__main__" :
    main ()