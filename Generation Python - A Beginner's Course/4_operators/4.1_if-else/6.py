"""
Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
сумма первой и последней цифр равна разности второй и третьей цифр.
"""

num = int(input())

a = num // 1000
b = (num // 100) % 10
c = num % 100 // 10
d = num % 10

if (a + d) == (b - c):
    print('ДА')
else:
    print('НЕТ')