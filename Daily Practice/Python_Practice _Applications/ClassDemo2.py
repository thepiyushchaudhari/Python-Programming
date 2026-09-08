class Demo :
    def __init__(self):                 #__init__ --> CONSTRUCTOR
        print("Inside Constructor")
        
    def __del__(self):
        print("Inside Destructor")      #__del__ --> DESTRUCTOR

#<<<<<OBJECTS OF CLASSS>>>>>
obj1 = Demo()
obj2 = Demo()

print("End of application")