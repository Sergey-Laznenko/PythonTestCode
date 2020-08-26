"""
Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
"""

num = int(input())
x = num % 10
answer = 'YES'
while num != 0:
    rez = num % 10
    if x != rez:
        answer = 'NO'
    num = num // 10
print(answer)
