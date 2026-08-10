def main():
    try:
        open("Demo.txt","w")    # w -> write
        print("File gets opened")

    except FileNotFoundError as fobj :
        print("File is not present in current Directory")

if __name__ == "__main__":
    main()