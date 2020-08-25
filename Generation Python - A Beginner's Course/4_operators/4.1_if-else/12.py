"""
Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
"""

a, b, c, = int(input()), int(input()), int(input())
total = 0
if a > 0:
    total += a
if b > 0:
    total += b
if c > 0:
    total += c
print(total)
