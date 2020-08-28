"""
На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов,
затем k строк — поисковые запросы. Напишите программу, которая выводит все введенные строки,
в которых встречаются все поисковые запросы.
"""

data = []
for _ in range(int(input())):
    string = input()
    data.append(string)

request = []
for _ in range(int(input())):
    key = input()
    request.append(key)
rez = []
for item in data:
    flag = True
    for key in request:
        if not (key.lower() in item.lower()):
            flag = False
    if flag:
        print(item)
