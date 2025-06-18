string = "i am xyz"
# o/p : "z yx mai"
# li = string[::-1]
# print(li)
# lst = string.split()
start = 0
end = len(string) - 1

if start < end:
    string[start] == '' or string[end] = '':
        start = start + 1
        end = end - 1
else:
    get = (string[start], string[end])
    (string[end], string[start]) = get

