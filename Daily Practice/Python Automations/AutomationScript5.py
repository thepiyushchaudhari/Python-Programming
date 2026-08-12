import sys

def main ():

    print("--"*50)
    print("Marvellous Automation Script")
    print("--"*50)

    if(len(sys.argv)== 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory.")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage")
            print("Pleas execute the script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
            
        else:    
            DirectoryName = sys.argv[1]
            print("Directory name is : ", DirectoryName)
    else:
        print("Invalid number of arguments")
        print("Use --h for help or --u for usage")
    
    print("--"*50)
    print("Thank You For Using Marvellous Automation Script")
    print("--"*50)
        

if __name__ == "__main__" :
    main()  