"""
На обработку поступает последовательность из 4 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10**6
Нужно написать программу, которая выводит на экран количество нечётных чисел в исходной последовательности и максимальное нечётное число.
Если нечётных чисел нет, требуется на экран вывести «NO». Программист торопился и написал программу неправильно.

Найдите все ошибки в этой программе:

n = 4
count = 0
maximum = 999
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = i
            break
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
"""

n = 4
count = 0
maximum = -10 ** 6 - 1
for _ in range(1, n + 1):
    x = int(input())
    if x % 2 == 1:
        count += 1
        if x > maximum:
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
