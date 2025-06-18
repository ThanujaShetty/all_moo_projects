"""t1 = ()
print(type(t1))
s1 = set()
print(type(s1))"""


############################################################
# Generators -->square
"""def square_num():
    i = 1
    while i < 20:
        yield i * i
        i += 1

print(list(square_num()))"""
############################################################
# cube_num = lambda num : num * 3
# print(cube_num(5))

############################################################
# def name_func(func):
#     def wrapper(*args,**kwargs):
#         print("function name :",func.__name__)
#         func (*args,**kwargs)
#     return wrapper
#
# @name_func
# def add(a , b, c):
#     print( a + b + c)
#
# add(1, 2, 3)

############################################################
# string = "hello sony"
# for item in enumerate(string):          # item --> (0, "h")
#     print(item[0], item[1], end=", ",)
#
#
#     class Shape:
#         def area(self):
#             pass
#
#
#     class Circle(Shape):
#         def area(self, radius):
#             return 3.14 * radius ** 2
#
#
#     class Square(Shape):
#         def area(self, side):
#             return side ** 2
#
#
#     # Creating instances of the subclasses
#     circle_instance = Circle()
#     square_instance = Square()
#
#     # Calling the area method of each subclass
#     print(circle_instance.area(5))  # Output: 78.5
#     print(square_instance.area(4))  # Output: 16

# def print_mesg(func):
#     def wrapper(*args,**kwargs):
#         print("hello everone")
#         func(*args,**kwargs)
#     return wrapper
#
# @print_mesg
# def add(a,b):
#     print( a+b)
#
#
#
# add(1,3)

# single inheritance
# class Vehical:
#     def __init__(self,model,make):
#         self.model = model
#         self.make = make
#
#     def display_info(self):
#         return f"{self.model} {self.make}"
#
# class Car(Vehical):
#     def __init__(self,make,model,no_doors):
#         super().__init__(make,model)
#         self.no_doors = no_doors
#
#     def display_info(self):
#         return f"{super().display_info()} {self.no_doors}"
#
# my_car = Car("2021","fiat",4)
# print(my_car.display_info())

# i=0
# def repeat():
#     global i
#     if i == 3:
#         return
#     print("hello")
#     i += 1
#     repeat()
#
# repeat()

# l = enumerate([1,2,3])
# print(dict(l))

class Points:
    # class variables
    a = 12
    b = 14

    def __init__(self, a, b):       # instance variables
        self.a = a
        self.b = b


p1 = Points(1, 2)
p2 = Points(10, 20)

# __dict__ --> returns a dictionary of attributes present in the class or instances
print(Points.__dict__)      # class dictionary
print(p1.__dict__)          # instance dictionary
print(p2.__dict__)          # instance dictionary


