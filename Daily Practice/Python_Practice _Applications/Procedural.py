def Addition (No1, No2):
    Ans = No1 + No2
    return Ans

def Substraction(No1, No2):
    Ans = No1 - No2
    return Ans

print("Enter First Number : ")
Num1 = int(input())

print("Enter First Number : ")
Num2 = int(input())

Ret = Addition(Num1, Num2)
print("Addition is : ", Ret)

Ret = Substraction(Num1, Num2)
print("Substraction is : ", Ret)