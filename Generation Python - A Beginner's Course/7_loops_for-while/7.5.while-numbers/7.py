"""
Дано натуральное число. Напишите программу, которая вычисляет:
- сумму его цифр;
- количество цифр в нем;
- произведение его цифр;
- среднее арифметическое его цифр;
- его первую цифру;
- сумму его первой и последней цифры.
"""

num = int(input())
summa = 0
total = ''
pr = 1
while num != 0:
    n = num % 10
    summa += n
    total += str(n)
    pr *= n
    num = num // 10
print(summa)
print(len(total))
print(pr)
print(summa / len(total))
print(total[-1])
print(int(total[-1]) + int(total[0]))
