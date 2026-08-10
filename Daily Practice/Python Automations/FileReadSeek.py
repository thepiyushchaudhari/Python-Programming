#0 -> starting
#1 -> current
#2 - > ending

def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened")

        fobj.seek(10,0)     #from 10th offset onwards

        Data = fobj.read(20)

        print(Data)

    except FileNotFoundError as fobj :
        print("File is not present in current Directory")

if __name__ == "__main__":
    main()