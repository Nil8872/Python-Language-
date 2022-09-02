# biult-in function in python
# ex.: sum((a,b))

# a = (int)(input("Enter a: "))
# b = (int)(input("Enter b: "))
# d = sum((a,b))
# print("The sum of a and b is :", d)

# user define function 
# for create new function we will use def keyword
# ex. def function_name(arguments it it take):

# def printf():
#     print("My name is sariya nilesh ") 

# printf()
# printf()
# printf()
# printf()
# printf()

def function1(a,b):
    """This is fuction take two arguments and return average of those two values
        This fucntion only for two Arguments not others """
    """My name is nilesh"""
    c=(a+b)/2
    print(c)
    return c
# print(function1(3.5,5.3))
print(function1.__doc__)