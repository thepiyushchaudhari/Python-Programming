def main():
    try:
        fobj = open("Demo.txt","w")    # w -> write
        print("File gets opened")

        fobj.write("Jay Ganesh...")

        fobj.close()

    except FileNotFoundError as fobj :
        print("File is not present in current Directory")

if __name__ == "__main__":
    main()