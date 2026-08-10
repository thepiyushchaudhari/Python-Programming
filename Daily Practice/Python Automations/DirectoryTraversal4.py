import os

def main():
    for FolderName, SubFolder, FileName in os.walk("Marvellous"):
        print("Folder Name : ",FolderName)
        
        for fname in FileName :
            print("File Name : ", fname)
            

if __name__ == "__main__" :
    main()