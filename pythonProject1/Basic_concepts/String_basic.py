#check given num is palindrome
"""def plaindrome(iterable):
     rev_str = iterable[::-1]
     if iterable == rev_str:
          print("string is palindrome")
     else:
          print("not a palindrome")

plaindrome("Hello")
plaindrome("madam")"""
#########################################################################
#factorial
"""num = int(input("enter num"))
fact = 1
if num < 0:
     print("enter only positive number")
else:
     for i in range(1,num+1):
          fact = fact * i
     print("factroila of given num is ",fact)"""
#########################################################################
#fibbonnoci
"""num = int(input("enter range"))
n1 = 0
n2 = 1
count = 0
if num < 0:
     print("Invalid input")
elif num == 1:
     print(n1)
else:
     while count < num:
          print(n1)
          n = n1 + n2
          n1 = n2
          n2 = n
          count += 1"""
#########################################################################
#prime
"""first = 10
last = 50
for num in range(first,last+1):
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print("prime numbers are",num)"""
#########################################################################



