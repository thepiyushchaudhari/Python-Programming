CheckOdd = lambda x : True if x % 2 == 1 else False

def main ():
    num = int(input("Enter the number you want to check if odd : "))
    print(CheckOdd(num))

if __name__ == "__main__" :
    main()
    