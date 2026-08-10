import os

def main():
    try:
        os.remove("Demo.txt")

    except FileNotFoundError as fobj :
        print("File is not present in current Directory")

if __name__ == "__main__":
    main()