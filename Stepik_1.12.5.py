"""
Напишите программу, которая получает на вход три целых числа,
по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное,
после чего оставшееся число.
"""

n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
n3 = int(input('Введите третье число: '))
if n1 >= n2 >= n3:
    print(f'max: ', n1)
    print(f'min: ', n3)
    print(f'mid: ',n2)
elif n1 >= n3 >= n2:
    print(n1)
    print(n2)
    print(n3)
elif n2 >= n1 >= n3:
    print(n2)
    print(n3)
    print(n1)
elif n2 >= n3 >= n1:
    print(n2)
    print(n1)
    print(n3)
elif n3 >= n1 >= n2:
    print(n3)
    print(n2)
    print(n1)
else: #6
    print(n3)
    print(n1)
    print(n2)