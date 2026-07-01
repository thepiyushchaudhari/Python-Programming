'''
input : 5
output : 78.55

'''
def CircleArea (Num):
    pi = 3.142
    print(pi * Num * Num)
        
        
def main():
    num = int(input("Enter Radius number :"))  
    CircleArea(num)
   

if __name__ == "__main__":
    main ()
