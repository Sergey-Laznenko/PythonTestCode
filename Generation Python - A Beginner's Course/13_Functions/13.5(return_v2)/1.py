"""
Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа,
и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и
False в противном случае.
"""


def is_valid_triangle(x, y, z):
    if (x < (y + z)) and (y < (z + x)) and (z < (x + y)):
        return True
    else:
        return False


a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))
