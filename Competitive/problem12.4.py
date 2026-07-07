'''
input : 5
output : 1   2   3   4   5

'''
def PrintNums (Num):

    for i in range(1, Num+1 ):
        print(i)
        
def main():
    num = int(input("Enter a number :"))  
    PrintNums(num)
   

if __name__ == "__main__":
    main ()
