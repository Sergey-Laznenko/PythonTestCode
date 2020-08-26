"""
Дано натуральное число nn. Напишите программу, которая выводит значение суммы 1!+2!+3!+ ... +n!.
"""

n = int(input())
counter = 1
total = 0
for i in range(1, n + 1):
    counter *= i
    total += counter
print(total)
