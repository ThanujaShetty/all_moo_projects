"""s = "hi hello thanuja"

# reverse string
def rev_string(input_string):
    reversed = ""
    for char in input_string:
        reversed = char + reversed
    return reversed


obj = rev_string(s)
print(obj)"""
###############################################################################################
# get largest number from list
"""l = [10, 20, 109, 30, 45, 80, 90, 89, 100, 102]

def largest_num(numbers):
    if not numbers:
        return None

    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

obj = largest_num(l)
print(obj)"""
###############################################################################################
"""num = int(input("enter number"))
if num > 0:
    print("Number is Positive")
elif num == 0:
    print("Number is zero")
else:
    print("Number is negative")"""
###############################################################################################
"""def is_prime(n):
    if n <= 1:
        return False

    for i in range(2,n):
        if n % i == 0:yad ele
        
            return False
    return True

n = int(input("Enter Number: "))
if is_prime(n):
    print("Number is prime")
else :
    print("Number is not Prime")"""
###############################################################################################
# generate prime numbers
"""def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def generate_prime(number):
    prime=[]
    for n in range(2,number+1):
        if is_prime(n):
            prime.append(n)
    return prime

n = int(input("Enter Limit"))
obj = generate_prime(n)
print(obj)"""
###############################################################################################
"""num = int(input("Enter Number: "))
fact = 1
if num < 0:
    print("Number should be greater than zero")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num +1):
        fact = fact*i
    print(f"Factorial of {num} is :",fact)"""
###############################################################################################
"""# fibonacci
nterm = int(input("Enter Number:"))
n1, n2 = 0, 1
count = 0
if nterm <= 0:
    print("Enter valid number")
elif nterm == 1:
    print(f"Fibonacci of {nterm} is", n1)
else:
    while count < nterm:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count += 1"""
###############################################################################################
"""import csv

with open('employees.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'],row['pay'])

with open('employees.csv','r')as file:
    reader =csv.reader(file)
    for row in reader:
        print(row)"""
###############################################################################################
nterm = int(input("Enter any number"))
n1 ,n2 = 0, 1
count = 1
if nterm <= 0:
    print("Enter only positive number")
