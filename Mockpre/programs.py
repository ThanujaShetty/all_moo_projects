#decorators programs
#wpt decorate a function that prints "hello everyone" before executing any function

"""def print_mesg(func):
    def wrapper(*args,**kwargs):
        print("hello everyone")
        func(*args,**kwargs)
    return wrapper

@print_mesg
def add(a,b):
    print("Addition of two numbers", a+b)

add(1,4)"""

##########################################################################
# wpt print the function name of the decorated function before executing any decorator func

"""def display_name(func):
    def wrapper(*args,**kwargs):
        print("Decorated function name ",func.__name__)
        func(*args,**kwargs)
    return wrapper

@display_name
def check_even(num):
    if num % 2 == 0:
        print("even number")

check_even(4)"""
##########################################################################
# create a decorator which inputs 5 sec of delay before executing any functions
"""import time

def apply_delay(func):
    def wrapper(*args,**kwargs):
        # time.sleep(5)
        print("applyed wait for 5 sec",time.sleep(5))
        func(*args,**kwargs)
    return wrapper

@apply_delay
def sample():
    print("hello")
sample()"""
##########################################################################
# write a decorator to calculate execution time of any function
"""import time

def execution_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter_ns()
        res = func(*args,**kwargs)
        end_time = time.perf_counter_ns()
        return f"execution time {end_time -start_time}",f"result is {res}"
    return wrapper

@execution_time
def difference(a,b):
    print(a-b)

print(difference(8,2))"""

##########################################################################
# create a decorator which counts the no of function calls
"""count = 0
def fun_call(func):
    def wrapper(*args,**kwargs):
        global count
        print(f"executing {func.__name__} function")
        count += 1
        func (*args,**kwargs)
    return wrapper

@fun_call
def add(a,b):
    print("addtion",a+b)

@fun_call
def sub(a,b):
    print("subtraction",a-b)


add(3,4)
add(4,5)
sub(5,1)
print("number of func call",count)"""

##########################################################################
# create a decorator which returns only positive o/p for all subtraction function

# def return_positive(func):
#     def wrapper(*args,**kwargs):
#         print("returning positive no")
#         resuilt = func(*args,**kwargs)
#         pos = abs(resuilt)
#         return pos
#     return wrapper
#
# @return_positive
# def sub(a, b):
#     print(a-b)
#
# print(sub(15,19))

##########################################################################
# create a decorator that executes for 3 times

"""def outer(func):
    def wrapper(*args,**kwrgs):
        for i in range (3):
            func(*args,**kwrgs)
    return wrapper

@outer
def add(a,b):
    print(a+b)

add(2,3)"""
##########################################################################
# create a dictionary to count the number of function call
"""d = {}
def count_func_call(func):
    def wrapper(*args,**kwargs):
        if func.__name__ not in d:
            d[func.__name__] = 1
        else:
            d[func.__name__] += 1
        func(*args,**kwargs)
    return wrapper

@count_func_call
def add(a,b):
    print(a+b)

add(6,7)
add(5,6)
print(d)"""
##########################################################################
# create a decorator that counts the number of decorated function
"""count =0
def outer(func):
    global count
    count += 1
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
    return wrapper

@outer
def add(a,b):
    print(a + b)

@outer
def sub(a,b):
    print(a - b)

sub(5,3)
add(8,9)
add(5,7)
print(count)"""
##########################################################################
