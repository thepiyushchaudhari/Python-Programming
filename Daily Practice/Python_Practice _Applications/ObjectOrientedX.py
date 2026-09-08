class Arithematic :
    
    def Addition (self,No1, No2):
        Ans = No1 + No2
        return Ans

    def Substraction(self,No1, No2):
        Ans = No1 - No2
        return Ans

Aobj = Arithematic()

print("Enter First Number : ")
Num1 = int(input())

print("Enter First Number : ")
Num2 = int(input())

#Ret = Addition(Aobj,Num1,Num2)
Ret = Aobj.Addition(Num1, Num2)
print("Addition is : ", Ret)
#Ret = Substraction(Aobj,Num1,Num2)
Ret = Aobj.Substraction(Num1, Num2)
print("Substraction is : ", Ret)