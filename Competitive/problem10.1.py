'''
input : 4
output : 4  8   12  16  20  24  28  32  36  40

'''
def Table (No):

    for i in range(1,11):
        print(i * No)

def main():
    num = int(input("Enter a number :"))  
    Table(num)
    

if __name__ == "__main__":
    main ()
