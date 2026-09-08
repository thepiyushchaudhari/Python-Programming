no = 11      #Global Variable

def Display ():
    a = 21      #Local variable
    
    print("From Display : ", no)
    print("From Display Value of 'a' is  : ", a)

def Demo ():
    print("From Demo value of 'a' is :",a)  #---ERROR---
    print("From Demo : ", no) 

Display()
Demo() 