"""
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран произведение цифр введенного числа.
Программист торопился и написал программу неправильно.

Найдите все ошибки в этой программе:

n = input()
product = n % 10
while n >= 10:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)
"""

n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n //= 10
print(product)
