"""
Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. Если при этом введённое с клавиатуры число – ноль,
то вывести «Обратного числа не существует» (без кавычек).
"""

s = float(input())
if s != 0:
    print(s ** -1)
else:
    print('Обратного числа не существует')
