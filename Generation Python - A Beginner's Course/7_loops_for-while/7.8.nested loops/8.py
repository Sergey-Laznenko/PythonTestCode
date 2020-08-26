"""
Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием,
равным n в соответствии с примером:
"""

n = int(input())
for i in range(1, n // 2 + 2):
    print('*' * i)
for j in range(n // 2, 0, -1):
    print('*' * j)
