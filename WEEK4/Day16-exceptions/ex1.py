#an exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.
try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a 2nd number: "))
    print(f"the quotient is:{num1/num2} ")
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("enter an interger")
except Exception:
    print("an error occurred")  
