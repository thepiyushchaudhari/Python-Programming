def main():
    try:
        open("Demo.txt","r")    # r -> read
        print("File gets opened")

    except FileNotFoundError as fobj :
        print("File is not present in current Directory")

if __name__ == "__main__":
    main()