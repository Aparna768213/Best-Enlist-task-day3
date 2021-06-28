#Create a lambda function that multiplies argument x with argument y

multiply = lambda x, y:x*y

print(multiply(5, 9))

# Write a Python program to create Fibonacci series to n using Lambda

from functools import reduce

fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                       range(n - 2), [0, 1])

print(fib(5))

# Write a Python program that multiply each number of given list with a given number

my_list = [1, 2, 3, 4, 5]
my_new_list = [i * 5 for i in my_list]
print(my_new_list)

# Write a Python program to find numbers divisible by 9 from a list of numbers

my_list = [12, 65, 54, 72, 102, 27, 45,]

result = list(filter(lambda x: (x % 9 == 0), my_list))

print("Numbers divisible by 9 are",result)

# Write a Python program to count the even numbers in a given list of integers

my_list = [2,4,1,9,14,75,7,26]
result = list(filter(lambda x: (x%2==0),my_list))
print("even number from the list is:",result)