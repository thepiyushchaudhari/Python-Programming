'''
input : 15
output : Divisible by 3 and 5

'''
def ChecKDiv (No):
    
    if((No % 3 == 0) and (No % 5 == 0) ):
        print("Divisible by 3 and 5")
        
    elif(No % 3 == 0):
        print("Divisible by 3")
        
    elif(No % 5 == 0):
        print("Divisible by 5")
    
    else:
        print("Not divisible by 3 and 5")
        
def main():
    
    num = int(input("Enter a number :")) 
    ChecKDiv(num)    

if __name__ == "__main__":
    main ()
