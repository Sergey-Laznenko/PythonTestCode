"""
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран максимальную цифру числа,
кратную 3. Если в числе нет цифр, кратных 3, требуется на экран вывести «NO». Программист торопился и написал программу неправильно.

Найдите все ошибки в этой программе:

n = int(input())
max_digit = n % 10
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit < max_digit:
            digit = max_digit
    n = n % 10
if max_digit == 0:
    print('NO')
else:
    print(max_digit)
"""

n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)
