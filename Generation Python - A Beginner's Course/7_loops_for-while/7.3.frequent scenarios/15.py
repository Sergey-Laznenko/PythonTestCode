"""
Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.
"""

f1 = f2 = 1
n = int(input())

if n == 1:
    print(1)
else:
    print(f1, end=' ')
    print(f2, end=' ')

for _ in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
