Even = lambda x : x % 2 == 0 

def main ():
    Data = [11,12,13,14,15,16,17,18,19,20]
    print("Input Data : ", Data)
     
    FilterData = list(filter(Even, Data))
    print("Data after filter : ", FilterData)
       

if __name__ == "__main__":
    main ()  