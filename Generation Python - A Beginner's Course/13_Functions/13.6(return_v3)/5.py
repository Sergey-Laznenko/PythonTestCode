"""
Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты
квадратного уравнения ax**2 + bx + c = 0 и возвращает его корни в порядке возрастания.
"""


from math import sqrt


def solve(x, y, z):
    discriminant = (y ** 2) - 4 * (x * z)
    res_1 = ((-y - sqrt(discriminant)) / (2 * x))
    res_2 = ((-y + sqrt(discriminant)) / (2 * x))
    return min(res_1, res_2), max(res_1, res_2)


a, b, c = int(input()), int(input()), int(input())
x1, x2 = solve(a, b, c)
print(x1, x2)
