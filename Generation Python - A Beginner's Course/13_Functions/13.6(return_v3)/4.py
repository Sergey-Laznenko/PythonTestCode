"""
Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два значения:
длину окружности и площадь круга, ограниченного данной окружностью.
"""


from math import pi


def get_circle(radius):
    length_res = 2 * pi * radius
    square_res = pi * (radius ** 2)
    return length_res, square_res


r = float(input())

length, square = get_circle(r)
print(length, square)
