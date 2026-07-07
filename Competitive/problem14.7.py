Divisible = lambda x : True if x % 5 == 0 else False

def main():
    num = int(input("Enter number you want to check if divisible by 5 :"))
    print(Divisible(num))

if __name__ == "__main__":
    main()