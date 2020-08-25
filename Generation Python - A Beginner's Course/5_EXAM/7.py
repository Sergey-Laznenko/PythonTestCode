"""
Даны две различные клетки шахматной доски. Напишите программу,  которая определяет,
может ли конь попасть с первой клетки на вторую одним ходом
"""

x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')
