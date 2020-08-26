"""
Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной n,
в соответствии с примером:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
...
"""

n = int(input())
x = 1
for i in range(n + 1):
    for _ in range(i):
        print(x, end=' ')
        x += 1
    print()
