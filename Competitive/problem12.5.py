'''
input : 5
output : 5   4   3   2   1

'''
def RevPrintNums (Num):
    for i in range(Num, 0 , -1 ):
        print(i)
        
        
def main():
    num = int(input("Enter a number :"))  
    RevPrintNums(num)
   

if __name__ == "__main__":
    main ()
