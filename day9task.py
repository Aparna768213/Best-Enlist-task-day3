#WAP to loop through a list of numbers and add +2 to every value to elements in list
a=[10,20,30,40,50]
for i in a:
    print(i+2,end=" ")


#WAP to get the below pattern.
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


#python program to print the fibonacci sequence
def num(n):
    if n<0:
        print("number is less than zero")
    elif n==0:
        print("zero")
    elif n==1 or n==2:
        return 1
    else:
        return num(n-1)+num(n-2)
print(num(10))


#Explain Armstrong number and write a code with a function.
n=int(input("Enter a Number"))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if n==sum:
    print("Amstrong Number")
else:
    print("Not amstrong Number")



#WAPto print the multiplication table of 9
for i in range(1,11):
    print(9,"x",i,"=",i*9)


#Check if a program is positive or negative
x=int(input("Enter a program"))
if x>0:
    print("Positive")
else:
    print("Negative")


#WAP to convert the number of days to ages
x=int(input("Enter the no of days"))
if x<0:
    print("days cannot be negative")
elif x==0:
    print("days cannot be zero")
else:
    print("Ages",x//365)


#solve trigonometry problem using math function WAP to solve using math function
import math
x = int(input("Enter value"))
print(math.sin(x),"sin")
print(math.cos(x),"cos")
print(math.tan(x),"tan")


#creat a calculator only on a code level by using if condition .
a=int(input("num1 "))
b=int(input("num2 "))
c=input("Enter operator")
if c == '+':
    print("Addition of two numbers",a+b)
elif c=='-':
    print("Subtraction of two numbers",a-b)
elif c=='*':
    print("Multiplication of two numbers",a*b)
elif c=='/':
    if a==0:
        print("Numerator cannot be zero")
    elif b==0:
        print("Zero division error")
    elif a==0 and b==0:
        print("Zero")
    else:
        print("Division of two numbes",a/b)
else:
    print("not found")




