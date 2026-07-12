class Arithematic :
    
    def Addition (No1, No2): #self absent which gives error
        Ans = No1 + No2
        return Ans

    def Substraction(No1, No2):
        Ans = No1 - No2
        return Ans

Aobj = Arithematic()

print("Enter First Number : ")
Num1 = int(input())

print("Enter First Number : ")
Num2 = int(input())

#<<<ERROR WILL OCCUR>>>
Ret = Aobj.Addition(Num1, Num2)
print("Addition is : ", Ret)

Ret = Aobj.Substraction(Num1, Num2)
print("Substraction is : ", Ret)