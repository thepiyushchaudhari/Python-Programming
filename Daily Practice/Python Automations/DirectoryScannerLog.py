import sys, os

def DirectoryScanner(DirectoryPath):

    print("Files from the Directory are : ")
    
    fobj = open("MarvellousLog.txt", "w")
    fobj.write("Marvellous Automation Script\n")
    fobj.write("Files from the Directory are : \n")

    for FolderName, SubFolder, FileName in os.walk (DirectoryPath):
        for fname in FileName:
            fobj.write(fname + "\n")
    fobj.close()

def main ():

    Border = "--"*50
    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if(len(sys.argv)== 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory.")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Pleas execute the script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
            
        else:    
            DirectoryScanner(sys.argv[1])

    else:
        print("Invalid number of arguments")
        print("Use --h for help or --u for usage")
    
    print(Border)
    print("Thank You For Using Marvellous Automation Script")
    print(Border)

        

if __name__ == "__main__" :
    main()  