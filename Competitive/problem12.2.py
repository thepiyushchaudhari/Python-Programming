'''
input : 12
output : 1   2   6   12

'''
def Factors (Num):

    for i in range(1, Num + 1):
        if Num % i == 0:
            print(i)
        
def main():
    num = int(input("Enter a number :"))  
    Factors(num)
   

if __name__ == "__main__":
    main ()
