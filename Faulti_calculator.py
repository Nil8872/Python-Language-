print("Enter First number: ", end=" ")
var1 = (int)(input())
print("Enter second number: ", end=" ")
var2 = (int)(input())
print("Which Operation you want to perform ex: + - * or /")
var3 = input()

if(var3 == "+"):
    if(var1 == 56 and var2==9):
        print("The sum of Two number is : 77")
    else : print("The sum of Two number is : ",var1+var2 )
elif(var3=="-"):
    print("The sub of Two number is : ", var1-var2 )
elif(var3=="*"):
    if(var1 == 5 and var2==3):
        print("The sum of Two number is : 55")
    else : print("The mul of Two number is : ",var1*var2 )
elif(var3=="-"):
    if(var1 == 56 and var2==6):
        print("The sum of Two number is : 4")
    else : print("The sum of Two number is : ",var1/var2 )
else:print("Please Enter valid input!!!!....")