# import re
#
# print(re.findall(r'[Pp]ython','python is a programming lang Python is easy to learn python'))
# match = re.search(r'python','python programming, pyhon')
# print(match)
# print(match.group())
#
# print("checking string starts with : ", re.search(r'S[^u]','Snil'))
# print(re.search(r'[^a-z]','python programming'))
# print('Range',re.search(r'[a-zA-Z]',"123rthf"))
# print("Any char",re.search(r'p.th.n','python 3'))
# print('Date{mm-dd-yyyy}:',re.search(r'\[0-9]-[]'))

#########################################################################
file = open("Doc.txt","r")
line= file.readlines()
# for i in line:
#     print(i.strip())
#     file.close()

with open("Doc.txt","a") as file:
    file.write("java ")
    file.write("ruby")

with open("Doc.txt","w") as file:
    for i in reversed(line) :
        file.write(i)
        print(i.strip())

