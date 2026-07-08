
Divisible = lambda x : (x % 5 == 0) and (x % 3 == 0)
def main():
    Data = [11,12,13,14,15,16,17,18,19,20]
   
    FilteredData = list((filter(Divisible, Data)))
    print("Data after filtering : ", FilteredData)
    
if __name__ == "__main__" :
    main()

