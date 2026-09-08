class Base :
    def __init__(self):
        print("Inside Base Constructor")

class Derived(Base):
    def __init__(self):
        super().__init__() #to access parent class
        print("Inside Derived Constructor")
        
dobj = Derived()
