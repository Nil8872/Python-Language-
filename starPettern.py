from xmlrpc.client import boolean


n = (int)(input("how many rows you want to print: "))
num = (int)(input("Enter\n 1 for True\n 0 for False\n"))
if num==1:
    var = True
elif num == 0:
    var = False
else : print("Please enter valid Input!!")
i =n
j =n
if var == False :
    i = 0
    while i !=n :
        j = 0

        while j !=(n-i):
            print("*",end=" ")
            j +=1

        i += 1
        print()
else: 
    i = 0
    while i != n:
        j = 0
        while j != i+1:
            print("*",end=" ")
            j +=1 
        i += 1
        print()