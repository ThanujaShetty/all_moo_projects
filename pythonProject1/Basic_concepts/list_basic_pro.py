#1 Write a fuction that takes a tuple as input and returns a new tuple with the elements in the reverse order
class Basic_pro:

    def rev_tuple(self):
        li = tuple(input("enter numbers"))
        num = li[::-1]
        return num

# obj = Basic_pro()
# print(obj.rev_tuple())

#############################################################################################################
#2 Write a function that takes the tuple as an input and returns a new tuple with all the duplicate elements removed
    def remove_dulipcates(self):
        ele_dup = tuple(input("enter elements"))
        list_tup = list(ele_dup)
        new_li = []
        for num in list_tup:
            if num not in new_li:
                new_li.append(num)
        return tuple(new_li)
# obj = Basic_pro()
# print(obj.remove_dulipcates())
#############################################################################################################
#3 check weather string is symmetrical and palindrome
    def check_string(self,string):
        word = len(string)
        count = 0
        l1= word//2

        if word % 2:
            middle_ele = word //2 +1
        else :
            middle_ele = word // 2
        start = 0
        end = middle_ele
        while (start <middle_ele and end <word):
            if (string[start] == string[end]):
                start += 1
                end += 1
            else:
                count =1
                break
        if count== 0:
            print("Given string is symmetricl")
        else:
            print("given string is not symmetricl")
#
# obj = Basic_pro()
# obj.check_string("khokho")

#############################################################################################################
#4 Write a function that takes a list of numbers as input and returns the sum of all the numbers i n the list.
# Example:
# input_list = [1, 2, 3, 4, 5]
# output = 15
#     def sum_list(self,iterable):
#         sum = 0
#         for ele in iterable:
#             sum = ele + sum
#         return sum
# obj = Basic_pro()
# print(obj.sum_list([1,2,3,4]))
#############################################################################################################
#5 Given a string. The task is to print all words with even length in the given string
# input: s = "This is a python language"
# Output: This is python language

    def even_string(self,string):
        li = string.split()
        for ele in li:
            if len(ele)%2 == 0:
                print(str(ele),end=" ")

# obj = Basic_pro()
# obj.even_string("This is a python language two")
#############################################################################################################
#6 Write a function that takes a string as input and returns the reverse of the string
    def reverse_of_givenString(self,string):
        new_string = string[::-1]
        return new_string

# obj = Basic_pro()
# print(obj.reverse_of_givenString("hello world"))
#############################################################################################################
#7 how to get the maximum and minimum element in a set in Python, using the built-in function
# """s of Python. Examples:
# Input : set = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
#  Output : max is 65
#  Input : set = ([4, 12, 10, 9, 4, 13])
#  Output : min is 4"""

    def max_and_min(self,set):
        print("max is ",(max (set)))
        print("min is ",(min(set)))

# obj = Basic_pro()
# obj.max_and_min({8,16,24,1,25,3,10,65,55})
#############################################################################################################
#8 Given two lists a, b. Check if two lists have at least one element common in them.
# Examples:
# Input : a = [1, 2, 3, 4, 5]
#       b = [5, 6, 7, 8, 9]
#  Output : True
#  Input : a=[1, 2, 3, 4, 5]
#       b=[6, 7, 8, 9]
#  Output : False
    def comman_ele(self,a,b):

        for ele in a:
            if ele in b:
                return True
        return False

# obj = Basic_pro()
# print(obj.comman_ele([1, 2, 3, 4, 5],[5, 6, 7, 8, 9]))
#############################################################################################################
#9 Sort the dictionary by keys and values in Python. Here, iterkeys() returns an iterator over the dictionary’s keys
# key_value[2] = '56'
# key_value[1] = '2'
# key_value[4] = '12'
# key_value[5] = '24'
# key_value[6] = '18'
# key_value[3] = '323
    def sortdict(self,dictonary):
        d = {}
        keys = sorted(dictonary.keys())
        val = sorted(int(ele) for ele in dictonary.values())
        for key,value in zip(keys,val):
            if key not in d:
                d[key] = str(value)
        return d

d = { 1:'2',2:'56',4:'12',5:'24',6:'18',3:'323'}
# obj = Basic_pro()
# print(obj.sortdict(d))
#############################################################################################################






