#write a python script to merge two python dictionaries.
def Merge (dict1, dict2):
    return(dict2.update(dict1))
dict1 = {'a':10, 'b':20}
dict2 = {'c':30, 'd':40}
print(Merge (dict1, dict2))
print(dict2)



#WAP to sort the value from descending to ascending in list and convert it in to a set.
l=[20,5,15,0,10]
l.sort(reverse=True)
print(set(l))



#wap to swap cases of a given string.
s=input("Enter a string:")
print(s.swapcase())



#wAP to convert an integer to binary and octa decimal.
a=int(input("Enter a interger value:"))
print(bin(a))
print(oct(a))


#WAP to check the sum of three elements and divided by a value which is given as an input by the user.
total=0
l=[100, 200, 300]
for i  in range(0, len(l)):
    total = total + l[i]
print("Sum of three element is: ",total)
a=int(input("Enter a value "))
print("The division of the sum by the given value is:",total/a)



#WAP to find the repeated items of a list.
l=eval(input("Enter a list:"))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')


#WAP to get a string from a given string where all occurrencens of its first char have been changed to capital latter.
s=input("Enter a string:")
output=s[0].upper()+s[1:]
print(output)


#WAP to find mean,median and mode among three given numbers.
given_numbers = [1,2,2]
addition = 0
for i in given_numbers:
    addition = addition +i
print("addition",addition)
length = len(given_numbers)
mean = addition/length
print("mean :",mean)

given_numbers.sort()
if length%2==0:
    median1 = given_numbers[length//2]
    median2=given_numbers[length//2-1]
    median = (median1+median2)/2
else:
    median = given_numbers[length//2]
print("median is:",median)
import statistics
mode1=statistics.mode(given_numbers)
print("mode is :",mode1)

#WAP to list number of items in a dictionary key and sort the list with the help of a function and with out function.
dic1={'ravi':[12,13,14,76],'renu':[45,67,23,45],'anuj':[11,54,87,32]}
result={k:sorted(dic1[k]) for k in sorted (dic1)}
print(result)
#using function
def function(dic1):
    res =dict()
    for key in sorted(dic1):
        res[key]=sorted(dic1[key])
        return res
def function2(dic1):
    res=dict()
    for key in sorted(dict1):
     min1 = dic1[key]
    for key in sorted(dic1):
        if dic1[key]<min1:
            min1=dic1[key]
            res[key]=min1
    return res



