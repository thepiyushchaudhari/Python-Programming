SqrNum = lambda x : x * x

def main ():
    Data = [10,20,30,40,50,60,70,80,90,100]
    print("Input Data : ", Data)
    
    MapData = list(map(SqrNum, Data))
    print("Data after mapping : ", MapData)
    
    

if __name__ == "__main__":
    main ()  