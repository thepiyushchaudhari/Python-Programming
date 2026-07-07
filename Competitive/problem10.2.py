'''
input : 5
output : 15

'''

def SumOfN (No):
    Sum = 0
    for i in range(No+1):
        Sum =  i + Sum
    return Sum

def main():
    num = int(input("Enter a number :"))  
    Ret = SumOfN(num)
    print(Ret)
    

if __name__ == "__main__":
    main ()
