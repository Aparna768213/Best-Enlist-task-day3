#write a python script to merge two python dictionaries.
def Merge(dict1, dict2):
    return (dict2.update(dict1))
dict1 = {'ram':300,'harry':500}
dict2 = {'sita':600,'gita':900}
dict3 = Merge(dict1, dict2)
print(dict2)

#write a python program to remove a key from a dictionary.
dict = {'a':100, 'b':200, 'c':300, 'd':400, 'e':500}
print("dictionary items:", dict)
key = input("Enter a key present in the dict items that you want to remove:")
if key in dict:
    del dict[key]
else:
    print("this key is not present in the dictionary")
    exit(0)
print("Updated dictionary",dict)

#write a python program to map lists into a dictionary.
a = ['ram', 'sita', 'gita', 'shyama']
b = [100, 200, 300, 400]
c = dict(zip(a,b))
print(c)

#write a python program to find length of a set.
set = input("Enter a set")
print("The length of set is:",(len(set)))


#write a python program to remove the intersection of 2nd set from the 1st set.
set1 = {1,2,5,67,87,94}
set2 = {1,2,3,5,8,9,7}
print("\nRemove the intersection of 2nd set from the 1st set:")
for i in set1&set2:
    set1.remove(i)
print("set1: ",set1)

