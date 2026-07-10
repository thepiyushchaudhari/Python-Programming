import threading

def Display(No):
    print(f"Inside Display {No} : ", threading.get_ident())
    


def main ():
    
    print("Inside main : ",threading.get_ident())
    
    tobj = threading.Thread(target = Display, args = (11,)) #Comma makes the args an iterable(tuple)
    
    tobj.start()




if __name__ == "__main__":
    main ()