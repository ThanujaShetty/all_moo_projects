#program to reverse string
"""word = "hello"
print(word[::-1])"""

#with using inbuilt
"""rev_word ="".join(reversed(word))
print(rev_word)"""

######################################################################################################################
# program to check string is palindrome
#normal program

"""word = "madam"
rev_word = word[::-1]
if word == rev_word:
    print("palindrome")
else:
    print("not palindrome")"""

#optimized code
"""word = "madam"
pal = ["palindrome" if word == word[::-1] else "not palindrome"]
print("".join(pal))"""
######################################################################################################################
# reverse string
# word = "hello sony"
# print(word[::-1])"""


#using loops
"""rev_str = ""
for char in word:
    rev_str = char+rev_str
print(rev_str)"""

#optimzed code
"""rev_str = "".join([char for char in word[::-1]])
print(rev_str)"""
######################################################################################################################
# from abc import ABC, abstractmethod
#
# class MobilePhone(ABC):
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     @abstractmethod
#     def make_call(self, number):
#         pass
#
#     @abstractmethod
#     def send_message(self, number, message):
#         pass
#
# # Create concrete classes
# class AndroidPhone(MobilePhone):
#     def make_call(self, number):
#         return f"{self.brand} {self.model} - Calling {number} with Android."
#
#     def send_message(self, number, message):
#         return f"{self.brand} {self.model} - Sending message to {number} with Android: {message}"
#
# class IPhone(MobilePhone):
#     def make_call(self, number):
#         return f"{self.brand} {self.model} - Calling {number} with iPhone."
#
#     def send_message(self, number, message):
#         return f"{self.brand} {self.model} - Sending message to {number} with iPhone: {message}"
#
# android_phone = AndroidPhone(brand="Samsung", model="S20 ultra ")
# iphone = IPhone(brand="Apple", model="iPhone 15")
#
# print(android_phone.make_call("8976567840"))
# print(android_phone.send_message("8976567840", "Hello from Android!"))
# print(iphone.make_call("9876505678"))
# print(iphone.send_message("9876505678", "Hello from iPhone!"))
######################################################################################################################
"""word = "hellooo world"
c = 'o'
count = 0
for char in word:
    if char == c:
        count += 1
print(count)"""

"""def count_char(char,iterator):
    count = 0
    for ch in iterator:
        if ch == char:
            count += 1
    return count

result = count_char("o","helloooo world")
print(result)"""

#2nd way
count_char= "hellooo world"
character_counts = {char: count_char.count(char) for char in count_char}
# get count of 'o'
count_of_o = character_counts.get('o',0)
print(count_of_o)

#split 'o'
# word = "helloooo world"
# new_str = word.split('o')
# print(new_str)


word = "hello"
print(list(word))