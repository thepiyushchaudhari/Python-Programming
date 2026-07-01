'''
input : 5
output : 120

'''
def Factorial (No):
    Sum = 1
    for i in range(1,No+1):
        Sum =  i * Sum
    return Sum

def main():
    num = int(input("Enter a number :"))  
    Ret = Factorial(num)
    print(Ret)
    

if __name__ == "__main__":
    main ()