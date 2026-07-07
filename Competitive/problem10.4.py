'''
input : 10
output : 2  4   6   8   10

'''
def DisplayEven (No):
    Sum = 1
    for i in range(1,No+1):
        if(i % 2 == 0):
            print(i)


def main():
    num = int(input("Enter a number :"))  
    DisplayEven(num)


if __name__ == "__main__":
    main ()