
StrLen = lambda String : len(String) > 5
def main():
    Data = ["bmw", "mercedes", "lamborghini", "porsche", "ferrari"]
   
    FilteredData = list((filter(StrLen, Data)))
    print("Data after filtering : ", FilteredData)
    
if __name__ == "__main__" :
    main()

