CheckEven = lambda x : True if x % 2 == 0 else False

def main ():
    num = int(input("Enter the number you want to check if even : "))
    print(CheckEven(num))

if __name__ == "__main__" :
    main()
    