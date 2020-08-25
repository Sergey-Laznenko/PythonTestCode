"""
Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. Если число находится вне диапазона 1-10,
то программа должна вывести текст «ошибка».
"""

a = int(input())

if 1 <= a <= 10:
    if a == 1:
        print('I')
    elif a == 2:
        print('II')
    elif a == 3:
        print('III')
    elif a == 4:
        print('IV')
    elif a == 5:
        print('V')
    elif a == 6:
        print('VI')
    elif a == 7:
        print('VII')
    elif a == 8:
        print('VIII')
    elif a == 9:
        print('IX')
    elif a == 10:
        print('X')
else:
    print('ошибка')

# 2 вариант

a = int(input())
if a <= 0 or a > 10:
    print('ошибка')
elif a <= 3:
    print(a * "I")
elif a == 4:
    print((5 - a) * "I" + "V")
elif a <= 8:
    print("V" + (a - 5) * "I")
elif a <= 10:
    print((10 - a) * "I" + "X")
