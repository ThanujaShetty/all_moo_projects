# print negative numbers
"""min = int(input("enter min number"))
max = int(input("enter max number"))

for num in range(min, max):
    if num < 0:
        print(num, end="")"""

##############################################################################
"""from datetime import date

today = date.today()
print(today)"""

##############################################################################
"""def check_even_odd(number):
    if number % 2 == 0:
        print("Given number is even ")
    else:
        print("Given number is odd")


number = 11
obj = check_even_odd(number)"""
##############################################################################
# print fiboncci number
"""number = int(input("Enter Range"))
count = 0
n1 =0
n2 = 1
while count < number:
    if count <= 1:
        n = count
    else:
        n = n1 + n2
        n1 = n2
        n2 = n
    print(n,end =" ")
    count = count + 1"""
##############################################################################
# find factor of given number

"""number = int(input("Enter any integer:"))
value = 1
print("Factor of given number is :")
while (value<=number):
    if (number % value == 0):
        print(value,end =" ")
    value = value + 1"""
##############################################################################
# find factorial of given number

"""numbers = int(input("Eneter any value"))
fact = 1
count = 1
while(count <= numbers):
    if (numbers < 0):
        print("Enter only positive number")
    elif (numbers == 0):
        print("Factorial of 0 is 1")
    else:
        fact = fact * count
        count += 1
print(fact)"""
##############################################################################
# check number is plaindrome or not
"""number = int(input("enter number"))
reverse = 0
temp = number

while (temp > 0):
    n = temp % 10
    reverse = (reverse * 10) + n
    temp = temp //10

if number == reverse:
    print("given number is palindrome")
else:
    print("number is not palindrome")"""
##############################################################################
# print palindrome number till 100

"""number = int(input("Enter range"))
print(f"plaindrome number from 1 to {number} :")
for num in range(1,number+ 1):
    temp = num
    reverse = 0

    while (temp > 0):
        reminder = temp % 10
        reverse =(reverse * 10) + reminder
        temp = temp //10

    if (num == reverse):
        print(num,end=" ")"""
##############################################################################
# reverse number

"""number = int(input("Enter Number"))
reverse = 0
while(number > 0):
    reminder = number % 10
    reverse = (reverse * 10) + reminder
    number = number // 10
print("Reverse of given number is :",reverse)"""
##############################################################################
# find sum of given number

"""number = int(input("Enter Number"))
sum = 0

while( number > 0):
    reminder = number % 10
    sum = sum + reminder
    number = number // 10

print("Sum of given number is :",sum)"""
##############################################################################
# given string is palindrome or not

"""string = input("Enter string: ")
rev = string[::-1]
if string == rev:
    print("Given string is palindrome")
else:
    print("Not palindrome")"""
##############################################################################
# check number is prime

"""number = int(input("Enter any value: "))
count = 0

for i in range(2,number//2 +1):
    if (number % i == 0):
        count += 1
        break

if (count == 0 and number != 1):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")"""
##############################################################################
"""for number in range(1,100):
    count = 0
    for i in range(2,number//2+1):
        if(number % i == 0):
            count += 1
            break

    if(count ==0 and number != 1):
        print(number,end=" ")"""
##############################################################################
"""import json

data ={"name":"thanuja","Age":28}
res = json.dumps(data)
print(res)"""
##############################################################################
# Define custom exception
# class InsufficientFundsError(Exception):
#     def __init__(self, message="Withdrawal amount exceeds available balance."):
#         self.message = message
#         super().__init__(self.message)
#
#
# # Bank Account class
# class BankAccount:
#     def __init__(self, customer_name, balance):
#         self.customer_name = customer_name
#         self.balance = balance
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise InsufficientFundsError
#         self.balance -= amount
#         print(f"Withdrawal successful. New balance: ${self.balance}")
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposit successful. New balance: ${self.balance}")
#
# # Example usage
# try:
#     account = BankAccount("Alice", 500)
#     print(f"Customer: {account.customer_name}, Balance: ${account.balance}")
#     account.withdraw(700)  # This will trigger the custom exception
# except InsufficientFundsError as e:
#     print(e)
####################################################################################
"""students = {
    'rahul': {'math': 89, 'science': 90, 'english': 80},
    'ram': {'math': 99, 'science': 98, 'english': 87},
    'sham': {'math': 89, 'science': 70, 'english': 80}
}
total_marks = {name : sum(marks.values()) for name, marks in students.items()}
print(total_marks)

sorted_students = sorted(total_marks.items(),key=lambda item : item[1], reverse=True)
print(sorted_students)

for rank,(name,total) in enumerate(sorted_students,1):
    print(f"{rank}.{name.capitalize()} - Total Marks ={total}")

"""
####################################################################################
# sort string
"""string = input("Enter Any string")
sorted_string = "".join(sorted(string))
print(sorted_string)
"""
##########################################################################################
# Find second largest score in math
"""students = {
    'rahul': {'math': 89, 'science': 90, 'english': 80},
    'ram': {'math': 99, 'science': 98, 'english': 87},
    'sham': {'math': 60, 'science': 70, 'english': 80},
    'bham': {'math': 190, 'science': 70, 'english': 80}
}

math_score = [students['math'] for students in students.values()]
print(math_score)

first = second = 0
for score in math_score:
    if score > first:
        second = first
        first = score
    elif first > score > second:
        second = score
print("Second largest score",second)"""

##########################################################################################
"""students = {
    'rahul': {'math': 189, 'science': 90, 'english': 80},
    'ram': {'math': 99, 'science': 98, 'english': 87},
    'sham': {'math': 79, 'science': 70, 'english': 80},
    'bham': {'math': 120, 'science': 70, 'english': 80},
    'rham': {'math': 30, 'science': 70, 'english': 80}
}

math_score = [student['math'] for student in students.values()]
print(math_score)
largest = 0
for score in math_score:
    if score > largest:
        largest = score
print("largest math score",largest)"""
##########################################################################################
"""deep_list = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
element = deep_list[2][2][0]
print(element)  # Output: eee"""
##########################################################################################
"""matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
column_elements = [row[2] for col in matrix]
print(column_elements)  # Output: [2, 5, 8]"""
##########################################################################################
"""import re
phn_no = "6237323789"
for num in phn_no:
    if re.match(r"^(?:\+91[\-\s]?)?[6789]\d{9}$",phn_no) :
        print("matched ")
    else:
        print("Not matched")"""

############################################################################################
"""def is_monotonic(nums):
    increasing = decreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        elif nums[i] < nums[i - 1]:nam 
            increasing = False

    return increasing or decreasing

# Example usage:
nums = [1, 2, 2, 3]
print("Is monotonic:", is_monotonic(nums))  # Output: True

nums = [6, 5, 4, 4]
print("Is monotonic:", is_monotonic(nums))  # Output: True

nums = [1, 3, 2]
print("Is monotonic:", is_monotonic(nums))  # Output: False"""
############################################################################################

