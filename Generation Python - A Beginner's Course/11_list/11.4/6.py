"""
На вход программе подается натуральное число nn, затем nn строк, затем еще одна строка — поисковый запрос.
Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
"""

data = []
for _ in range(int(input())):
    s = input()
    data.append(s)
key = input()
for item in data:
    if key.lower() in item.lower():
        print(item)
