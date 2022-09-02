n = 25


no_of_guess = 10
a = 1
while(no_of_guess !=0):
    print("Enter the number : ", end=" ")
    var = (int)(input())
    if(var>n):
        print("lesser!")
    elif(var==n):
        print("You won! your guess is : ",a)
        break
    elif(var<n):
        print("Greter!")
    else :
        print("please enter valid input!")
    no_of_guess = no_of_guess - 1
    a = a+1
    print("Now your guess is ", no_of_guess)
    if no_of_guess==0:
        print("Game Over, Better luck next time!")

 