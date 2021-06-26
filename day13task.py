# 1.Write a Python program for all the cases which can check a string contains only a
# certain set of characters (in this case a-z, A-Z and 0-9).

import re

if __name__== "main_":
    string = input("Enter the string:")
    pattern = re.compile("[A-za-z0-9]+")

    if pattern.fullmatch(string) is not None:
        print("Found match:", string)

    else:
        print("Match not found")

# 2.Write a Python program that matches a word containing 'ab'.

import re

def check(string):

    pattern = re.compile("ab+\w*")

    match_object = pattern.findall(string)

    if len(match_object) != 0:

        for word in match_object:
            print(word)

    else:
        print("No match")

if __name__ == '_main_':
    string = input("enter string:")

    check(string)

# 3.Write a Python program to check for a number at the end of a word/sentence.

import re

def check(string):
    pattern = re.compile("[0-9]$")
    match_object = pattern.findall(string)

    if len(match_object) != 0:

        for word in match_object:
            print(word)

    else:
        print("No match")


if __name__ == '_main_':
    string = input("enter string:")

    check(string)

# 4.Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string

import re

results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))

# 5.Write a Python program to match a string that contains only uppercase letters

import re

if __name__== "main_":
    string = input("Enter the string:")
    pattern = re.compile("[A-Z]+")

    if pattern.fullmatch(string) is not None:
        print("Found match:", string)

    else:
        print("match not found")