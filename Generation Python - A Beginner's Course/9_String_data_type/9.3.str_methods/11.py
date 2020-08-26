"""
На вход программе подается строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
"""

text = input()
count = 0
for i in text:
    if i in "abcdefghijklmnopqrstuvwxyz":
        count += 1
print(count)
