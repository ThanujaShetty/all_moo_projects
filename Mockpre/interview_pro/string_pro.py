# 						Strings
# 1.	Program to check if the given datatype is of string datatype
"""check_str = 123
if isinstance(check_str,str):
    print("given input is of string datatype")
else:
    print("given input is of not string type")"""
########################################################################################33
# 2.	program to print elements present in even index
"""even_ele = "hello welcome to python"
for index,char in enumerate(even_ele):
    if index %2 == 0:
        print((index,char),end="")"""
########################################################################################33
# 3.	program to print alternate characters in the string
"""alternate_char = "hello welcome to python"
print(alternate_char[::2])"""
########################################################################################
# 4.	program to reverse a string using slicing
"""rev_string = "thanuja"
print(rev_string[::-1])"""
########################################################################################
# 5.	"program to convert uppercase to lowercase characters with and without inbuilt methods."
"""upper_to_lower = "HELLO THANUJA"
for char in upper_to_lower:
    if ord("A") <= ord(char) <= ord("Z"):
        print(chr(ord(char)+32),end=" ")"""

########################################################################################
# 6.	"program to convert lowercase to uppercase characters with and without inbuilt methods."
"""lower_to_upper = "hello thanuja"
for char in lower_to_upper:
    if ord("a") <= ord(char) <= ord("z"):
        print(chr(ord(char)-32),end="")"""
########################################################################################
# 7.	"program to swap the case in the given string with and without inbuilt methods"
"""swap_case = "HELLO"
for char in swap_case:
    if ord("a") <= ord(char) <= ord("z"):
        print(chr(ord(char)-32),end = "")
    elif ord("A") <= ord(char) <= ord("Z"):
        print(chr(ord(char)+32),end = "")"""
########################################################################################
# 8.	program to check if a substring is present in the string or not
"""def check_substring(main_string, substring):
    if substring in main_string:
        print(f"The substring '{substring}' is present in the string.")
    else:
        print(f"The substring '{substring}' is not present in the string.")

# Example usage:
main_string = "Hello, world!"
substring_to_check = "world"

check_substring(main_string, substring_to_check)"""
########################################################################################
# 9.	"program to extract numeric values from the string with and without inbuilt methods"
"""string = "hello welcome to 123 sony56 python 67"
for char in string:
    if char.isdigit():
        print(char,end="")"""
#######################################################################################
# 10.	"program to extract alphabetical values from the string with and without inbuilt methods"
"""string = "hello welcome to 123 sony56 python 67"
for char in string:
    if ord("a") <= ord(char) <= ord("z") or ord("A") <= ord(char) <= ord("Z"):
        print(char,end="")"""
#######################################################################################
# 11.	program to extract only special characters from the string with and without inbuilt methods
"""only_spl = "hello^7%$# welcome"
for char in only_spl:
    if char.isalpha():
        pass
    elif char.isdigit():
        pass
    else:
        print(char,end = " ")"""
#######################################################################################
# 12.	program to extract both alpha numeric values from the string with and without inbuilt methods
#######################################################################################
# 13.	Write a program to check if the given string is Palindrome or not with and without using reversed method.
# without reversed method
# string = "hello"
"""string = "madam"
rev_str = string[::-1]
if string == rev_str:
    print("given string is palindrome")
else:
    print("given string is not palindrome")"""
#######################################################################################
# 14.	Replace "how" to "who" in the string "hi how are you" with and without inbuilt methods
#with inbuilt- method
# """string = "hi how are you"
# print(string.replace("how","who"))"""
#
# #without using in-built function
# string = "hi how are you"
# new_lis = string.split()

#######################################################################################
# 15.	Replace all the vowels with "*" in the string "hello world"
"""replace_vowels = "hello python "
for char in replace_vowels:
    if char in "aeiouAEIOU":
        char = "*"
    print(char,end="")"""
#######################################################################################
# 16.	Replace all the characters which occurs more than once with "*" in the string "hello world"
"""string = "hello world"
for char in string:
    if string.count(char) > 1:
        char = "*"
    print(char,end="")"""
#######################################################################################
# 17.	"Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java"
"""file_name = input("enter file name with extension: ")
ext_ = file_name.split(".")
print(ext_[1])"""
#######################################################################################
# 18.	convert a string to a list and vice-versa.
# string to list
"""string = "hello world"
print(type(string))
new_str = string.split()
print(type(new_str))"""

#list to string
"""li = ['hello','welcome']
print(type(li))
conv = "".join(li)
print(type(conv))"""
#######################################################################################
# 19.	Covert the string "Hello welcome to Python" to a comma separated string.
"""string = "Hello welcome to Python"
new_str = string.split()
print(",".join(new_str))"""
#######################################################################################
# 20.	Write a Program to print ascii values of the characters present in a string.
"""value_str = "hello"
for char in value_str:
    print(ord(char),end=" ")"""
#######################################################################################
# 21.	"Find the longest word in the sentence
"""sentence = "Hello world. Welcomeim to Pythonii"
longest = ""
len_sen = sentence.split()
for ele in len_sen:
    if len(ele) >= len(longest):
        longest = ele
print(longest)"""
#######################################################################################
# 22.	"Sum all the numbers in the below string.
"""s = "Sony12India567Pvt2ltd"
sum = 0
for char in s:
    if char.isdigit():
        sum = sum + int(char)
print(sum)"""
#######################################################################################
# 23.	"Program to print the number of occurrences of characters in a String without using inbuilt functions.
"""s = 'helloworld'
d = {}
for char in s:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1
print(d)"""
#######################################################################################
# 24.	" Program to print only the repeated characters and count of the same.
"""s = 'helloworld'
d = {}
for count,char in enumerate(s):
    if s.count(char) > 1:
        if char not in d:
            d[char] = s.count(char)
print(d)"""
#######################################################################################
# 25.	Write a program to get alternate characters of a string
"""string = "hello welcome"
print(string[::2])"""
#######################################################################################
# 26.	"Find the longest non-repeated substring in the below string
"""s = "This is a Programming language and Programming is fun"
longest = ""
new_s = s.split()
d = {}
for ele in new_s:
        if ele not in d:
            d[ele] = 1
        else:
            d[ele] += 1
print(d)
for key,value in d.items():
    if value == 1:
        if len(longest) < len(key):
            longest = key
print(longest)"""
#######################################################################################
# 27.	Write a program to count the number of white spaces in a given string
# 28.	Write a program to rotate characters in a string
# 29.	Write a program to print only non-repeated characters in a string
# 30.	Write a program to print all the consonants in a given string
# 31.	Write a program to count no of capital letters in a string
# 32.	Write a program to find the first repeating character in a string
# 33.	" Write a program to find the index of nth occurrence of a sub-string in a string
# >>> sentence = ""hello world welcome to python hello hi how are you hello there"""
# 34.	"Write a program to count the number of occurrences of non-special characters in a given string
# >>> s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'"
# 35.	"Filter only those characters except digits
# s = '@hello12world34welcome!123'"
# 36.	"Find all max length words from the below sentence
# >>> sentence = ""hello world hi apple you yahoo to you"""
#
