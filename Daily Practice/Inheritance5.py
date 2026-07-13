class Base :
    print("Inside Base Constructor ")
    def fun(self):
        print("Inside fun of Base")
    
class Derived(Base):
   def sun(self):
       print("Inside Derived sun")
        
dobj = Derived()

dobj.fun()
dobj.sun()
