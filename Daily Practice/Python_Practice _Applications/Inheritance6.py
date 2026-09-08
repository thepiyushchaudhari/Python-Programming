class Base1 :
    def fun(self):
        print("Inside fun of Base1")
   
class Base2 :
    def gun(self):
        print("Inside gun of Base2")     

class Derived(Base1, Base2):        #---Multiple Inheritance---#
   def sun(self):
       print("Inside Derived sun")
        
dobj = Derived()

dobj.fun()
dobj.sun()
dobj.gun()
