no = 11 

def Display ():
   global no #updates the value of first no
   no = 21
   print("From Display", no)

print("Before : ", no)

Display()

print("After : ", no)
