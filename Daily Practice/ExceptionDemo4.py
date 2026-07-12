def main ():
    Ans = 0
    try:
        print ("Enter first number : ")
        No1 = int(input())
        
        print ("Enter second number : ")
        No2 = int(input())
    
        Ans = No1 / No2
        
        print("Division is successfull")

    except ZeroDivisionError as zobj :              #Specific Exception -> works for this error only 
        print("Exception Occured due to second operand is ZERO : ", zobj)
    
    except ValueError as vobj :                     #Specific Exception -> works for this error only 
        print("Exception occured due to invalid data type : ", vobj)
    
    except Exception as eobj :                      #Generic Exception -> works for any error while run time
        print("Exception occured : ", eobj)
        

    print("Result is : ", Ans)  

if __name__ == "__main__":
    main()