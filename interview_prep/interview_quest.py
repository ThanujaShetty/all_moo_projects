# 1 Write a program to find the length of the string without using inbuilt function (len)
"""def count_char(input_str):
    count = 0
    for char in input_str:
        if char.isalnum():
            count += 1
    return count


input_str = input("Enter any sentance")
obj = count_char(input_str)
print(obj)"""

#############################################################################################
# 2 Write a program to reverse a string without using any inbuilt functions.
"""def reverse_string(input_string):
    rev_str = ""
    for char in input_string[::-1]:
        rev_str = char
        print(rev_str,end="")


input_string = input("Enter String")
obj = reverse_string(input_string)"""
#############################################################################################
# 3  Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".
"""string = "Hi universe"
new_str = string.replace('universe','thanuja')
print(new_str)"""
#############################################################################################
# 4  How to convert a string to a list and vice-versa
"""string_ = "Hello hi welcome to python programming"
li = string_.split()
print(li)
str_ = " ".join(li)
print(str_)"""
#############################################################################################
# 6. Write a program to print alternate characters in a string.
"""string = "pythonselenium"
print(string[::2])"""
#############################################################################################
# 7. Write a Program to print ascii values of the characters present in a string.
"""st = "Hello Hi"
for char in st:
    print(ord(char),end=" ")"""
#############################################################################################
# 8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.
