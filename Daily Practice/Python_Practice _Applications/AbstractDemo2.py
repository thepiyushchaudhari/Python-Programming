from abc import ABC, abstractmethod             # ABC = Abstract Base Class is a class in abc library

class Base(ABC) :
    
    @abstractmethod
    def Addition(self, No1, No2):   #Abstract --> method without body
        pass
    

class Derived(Base):
    def Addition(self, No1, No2):   #Concrete --> method with body
        return No1 + No2


dobj = Derived()
Ret = dobj.Addition(10,11)
print("Addition is : ",Ret) 