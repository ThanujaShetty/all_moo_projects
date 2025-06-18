# function to check palindrome
"""def check_palindrome(input_str):
    rev = ""
    for char in input_str[::-1]:
        rev += char
    if rev == input_str:
        print("Palindrome")
    else:
        print("Not palindrome")


in_str = "madam"
obj = check_palindrome(in_str)"""
##################################################################################
# find missing nummber in list
li = [1, 2, 3, 4, 6,7,9]


def find_missing(num):
    n = len(num) + 2
    total = n * (n + 1) // 2
    actual_sum = sum(num)
    return total - actual_sum


obj = find_missing(li)
print(obj)
