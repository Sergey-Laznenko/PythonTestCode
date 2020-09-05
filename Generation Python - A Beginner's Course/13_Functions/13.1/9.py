"""
Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10
"""


def draw_triangle():
    height = 10
    for i in range(0, height + 1):
        print('*' * i)


draw_triangle()
