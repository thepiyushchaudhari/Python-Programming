'''
input : 75
output : Distinction

'''
def Grade (Num):
    
    if(Num >= 75):
        print("Distinction")
    elif(Num >= 60):
        print("First Class")
    elif(Num >= 50):
        print("Second Class")
    else:
        print("Fail")
    
        
        
def main():
    num = int(input("Enter your marks :"))  
    Grade(num)
   

if __name__ == "__main__":
    main ()
