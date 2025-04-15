def addition (x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    if y!=0:
        return x/y
    else:
        print("division by zero is not possible")

num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))

result=addition(num1,num2)
print(f"the sum is {result}")

result=subtraction (num1,num2)
print(f"the difference is {result}")

result=multiplication(num1,num2)
print(f"the product is {result}")

result=division(num1,num2)
print(f"the division is {result}")






 




