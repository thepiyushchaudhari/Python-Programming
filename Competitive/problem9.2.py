'''
input : 10 20
output : 20 is greater

'''
def CheckGreater (No1, No2):
    if(No1 > No2):
        print ("First number is greater")
    else:
        print("Second number is greater")

def main():
    num1 = int(input("Enter first number :")) 
    num2 = int(input("Enter second number :")) 
    CheckGreater(num1, num2)
    

if __name__ == "__main__":
    main ()
