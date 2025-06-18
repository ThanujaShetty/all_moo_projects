# Python Program to Count Number of Digits in a Number
"""Number = int(input("Please Enter any Number: "))
Count = 0
while(Number > 0):
    Number = Number // 10
    Count = Count + 1

print("\n Number of Digits in a Given Number = %d" %Count)"""
####################################################################################
# Python Program to check if a Number is Odd or Even
"""number = int(input(" Please Enter any Integer Value : "))

if(number % 2 == 0):
    print("{0} is an Even Number".format(number))
else:
    print("{0} is an Odd Number".format(number))"""
####################################################################################
# Python Program to Print Even Numbers from 1 to N using For Loop
"""maximum = int(input(" Please Enter the Maximum Value : "))

for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))"""
####################################################################################
# Python Program to Calculate Square of a Number""
"""number = float(input(" Please Enter any numeric Value : "))

square = number * number

print("The Square of a Given Number {0}  = {1}".format(number, square))"""
####################################################################################
# fins square root
"""import math

num = float(input(" Please Enter any numeric Value : "))

squareRoot = math.sqrt(num)

print("The Result Of {0}  = {1}".format(num, squareRoot))"""
####################################################################################
# Python Program to find all divisors of an integer
"""num = int(input("Please enter any integer to find divisors = "))

print("The Divisors of the Number = ")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)"""
####################################################################################
# Python Program to Read 10 Numbers and Find their Sum and Average
"""Sum = 0

print("Please Enter 10 Numbers\n")
for i in range(1, 11):
    num = int(input("Number %d = " %i))
    Sum = Sum + num

avg = Sum / 10

print("The Sum of 10 Numbers     = ", Sum)
print("The Average of 10 Numbers = ", avg)"""
####################################################################################
# Python Fibonacci Series program
"""Number = int(input("\nPlease Enter the Range : "))

# Initializing First and Second Values
i = 0
First_Value = 0
Second_Value = 1

# Find & Displaying
while (i < Number):
    if (i <= 1):
        Next = i
    else:
        Next = First_Value + Second_Value
        First_Value = Second_Value
        Second_Value = Next
    print(Next)
    i = i + 1"""
####################################################################################
# Python Program to find Factors of a Number using For Loop
"""val = int(input("Please Enter any Value : "))

print("Result of a Given {0} are:".format(val))

for i in range(1, val + 1):
    if(val%i == 0):
        print("{0}".format(i))"""
####################################################################################
# Python Program to find the Factorial of a Number using For Loop
"""number = int(input(" Please enter any Number : "))
fact = 1

for i in range(1, number + 1):
    fact = fact * i
print("The factorial of %d  = %d" %(number, fact))"""
####################################################################################
# Python Program to find First Digit of a Number

"""number = int(input("Please Enter any Number: "))

first_digit = number

while (first_digit >= 10):
    first_digit = first_digit // 10

print("The First Digit from a Given Number {0} = {1}".format(number, first_digit))"""
####################################################################################
# Python Program to find the Last Digit in a Number
"""
number = int(input("Please Enter any Number: "))

last_digit = number % 10

print("The Last Digit in a Given Number %d = %d" %(number, last_digit))"""
####################################################################################
# Python Program to Check Palindrome Number using for loop
"""num = int(input("Enter any Value: "))
rev = 0
temp = num

for _ in range(len(str(num))):
    rem = num % 10
    rev = (rev * 10) + rem
    num //= 10
if temp == rev:
    print('Palindrome')
else:
    print("Not")"""
####################################################################################
# Python Program to find Prime Number using For Loop
"""Number = int(input("Please Enter any Value: "))
count = 0

for i in range(2, (Number//2 + 1)):
    if(Number % i == 0):
        count = count + 1
        break

if (count == 0 and Number != 1):
    print(" %d is a Prime" %Number)
else:
    print(" %d is Not" %Number)"""
####################################################################################
# Python Program to print Prime Numbers from 1 to 100 using For Loop
"""for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')"""
####################################################################################
# Python Program to Reverse a Number using for loop
"""num = int(input("Enter any Number = "))

rv = 0

for i in range(len(str(num))):
    rv = rv * 10 + num % 10
    num = num // 10

print("The Result = ", rv)"""
####################################################################################
# Python Program to Find Sum of Digits of a Number using While Loop
"""Number = int(input("Please Enter any Number: "))
Sum = 0

while(Number > 0):
    Reminder = Number % 10
    Sum = Sum + Reminder
    Number = Number //10

print("\n Sum of the digits of Given Number = %d" %Sum)"""
####################################################################################
# Python Program to find All Occurrence of a Character in a String
"""str1 = input("Please enter your own String : ")
ch = input("Please enter your own Character : ")

for i in range(len(str1)):
    if(str1[i] == ch ):
        print(ch, " is Found at Position " , i + 1)"""
####################################################################################