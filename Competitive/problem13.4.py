'''
input : 123
output : 1111011

'''
def BinNum (Num):
    binary = bin(Num)[2:]
    print(binary)
        
        
def main():
    num = int(input("Enter a number :"))  
    BinNum(num)
   

if __name__ == "__main__":
    main ()
