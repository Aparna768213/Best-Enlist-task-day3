# 1.List down all the error types and check all the errors using a python program for all errors

num1 = int(input("Enter num1:"))
num2 = int(input("Enter a number to check the error"))

try:
    print(num1/num2)
    k = int(input("Enter a number:"))
    print(k)
except ZeroDivisionError as e:
    print("Zero division error:",e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("something went wrong....")

# 2.Design a simple calculator app with try and except for all use cases
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a, b):
    return  a/b



num1 = float(input("Enter first number:"))

op = input("select operator which you want to print:")

num2 = float(input("Enter second number"))

try:
    if op == '+':
        print(num1, '+', '=', add(num1, num2))

    elif op == '-':
        print(num1, '-', '=', subtract(num1, num2))
    elif op == '*':
        print(num1, '*', '=', multiply(num1, num2))
    elif op == '/':
        print(num1, '/', '=', divide(num1, num2))


except Exception as e:
    print("Something went wrong")

# 3.print one message if the try block raises a NameError and another for other errors

def message():
    try:
        name = "Aparna"
    except NameError:
        return "NameError occured. Some variable isn't defined."
print(message())