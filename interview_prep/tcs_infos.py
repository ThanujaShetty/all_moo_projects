# 1.	Create a dictionary with character and count pair
"""s = 'abracadabraca'
d={}
for char in s:
    if char not in d:
        d[char] = 1
    else :
        d[char] += 1
print(d)"""
from collections import Counter

####################################################################################
# 2.	Create a dictionary with character and count pair only if the character is a vowel
"""s = "hello world"
d ={}
for char in s:
    if char.lower() in 'aeiou':
        d[char] = 1
    
print(d)"""
####################################################################################
# 3.	Create a list with the sum of items of two lists corresponding to their indices
"""a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

sum = [x+y for x, y in zip(a,b)]
print(sum)"""
# ###################################################################################
# 4.Write a program to create a dictionary to get only the duplicate items and the number of times the item is repeated in the list.
"""names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
d={}
count_dict = Counter(names)
dulpi = {ele:count for ele, count in count_dict.items() if count > 1}
print(dulpi)"""
# ###################################################################################
#5.	Write a program to get the indices of each item in the below list
"""names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# output should be - {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}
indices_dict = {}
for index,name in enumerate(names):
    if name in indices_dict:
        indices_dict[name].append(index)
    else:
        indices_dict[name] = [index]
print(indices_dict)"""
# ###################################################################################
#6 Write a program to get the below output
"""sentence = "hello world welcome to python programming hi there"
# o/p: d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming']}
li = sentence.split()
d = {}
for word in li:
    key = word[0]
    if key in d:
        d[key].append(word)
    else:
        d[key] = [word]
print(d)"""
##############################################################################################################
# 2.	Reverse the values in the dictionary if the value is of type String
"""d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
for key,value in d.items():
    if isinstance(value,str):
        d[key] = value[::-1]
    else:
        d[key] = value
print(d)"""
##############################################################################################################
# 4.	Program to print only the repeated characters and count of the same.
s = 'helloworld'
"""d={}
for char in s:
    if char not in d:
        if s.count(char)> 1:
            d[char] = 1
    else:
        d[char] += 1
print(d)"""
##############################################################################################################
# 5.	Write a program to replace value present in nested dictionary.
# Replace "nose" with "net"
"""d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
for key,value in d.items():
    if isinstance(value,dict):
        for k, v in value.items():
            if v == 'nose':
                value[k] = 'net'
print(d)"""
##############################################################################################################
# 7.	Write a program to find most common words in a given list.
"""words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into','my', 'eyes', "you're", 'under']

count_word = Counter(words)
print(count_word)
most_common = count_word.most_common(8)
for word,count in most_common:
    print(f"{word}:{count}",end=" ")"""
##############################################################################################################
# 8.	Write a program to get all the duplicate items and the number of times the item is repeated in the list.
"""names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
count_ele = Counter(names)
duplicate_ele = {ele : count for ele, count in count_ele.items() if count > 1 }
print(duplicate_ele)"""
##############################################################################################################
# 9.	Write a program to map a product to a company and build a dictionary with company and list of products pair
"""all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows', 'iOS', 'Google Drive', 'One Drive']
# Pre-defined products for different companies
apple_products = {'iPhone', 'Mac', 'iWatch'}
google_products = {'Gmail', 'Maps', 'Google Drive'}
msft_products = {'Windows', 'One Drive'}

company_product_map = {
    'apple_prod' : [],
    'Google_prod' : [],
    'msft_prod' : []
}

for product in all_products:
    if product in apple_products:
        company_product_map['apple_prod'].append(product)
    elif product in google_products:
        company_product_map['Google_prod'].append(product)
    elif product in msft_products:
        company_product_map['msft_prod'].append(product)
print(company_product_map,end=" ")"""
##############################################################################################################
# 10.	Grouping Flowers and Animals in the below list.
"""items = ['lotus-flower', 'lily-flower', 'cat-animal', 'sunflower-flower', 'python-programming','dog-animal','rose-flower','cow-animal','java-programming']
group_items ={}

for item in items:
    name, catgry = item.split('-')
    if catgry not in group_items:
        group_items[catgry] = []
    group_items[catgry].append(name)
print(group_items)"""
##############################################################################################################
# 11.	Grouping files with same extensions.
"""files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
Group_list ={}
for name in files:
    file_name, ext = name.split('.')
    if ext not in Group_list:
        Group_list[ext] = []
    Group_list[ext].append(file_name)
print(Group_list)"""
##############################################################################################################
# count number of words in a sentence in the form of dictionary. ignore special characters.
"""sentence = "Hi there! How are you:) How are you doing today!"
d ={}
for char in sentence:
    if char.isalpha():
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
print(d)"""
##############################################################################################################
# 13.	Grouping even and odd numbers
"""numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# o/p should be {1: [1, 3, 5, 7, 9], 0: [2, 4, 6, 8, 10]}"

grouped_ele ={}
for num in numbers:
    key = num % 2
    if key not in grouped_ele:
        grouped_ele[key] = []
    grouped_ele[key].append(num)
print(grouped_ele)"""
##############################################################################################################
# 14.	Write a program to get the indices of each item in the below list
"""names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# output should be: {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}
new_li ={}
for index, ele in enumerate(names):
    if ele in new_li:
        new_li[ele].append(index)
    else:
        new_li[ele] = [index]
print(new_li)"""
##############################################################################################################























