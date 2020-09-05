"""
Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10
"""


def draw_box():
    width = 10
    height = 14
    print('*' * width)
    for _ in range(height - 2):
        print('*' + ' ' * (width - 2) + '*')
    print('*' * width)


draw_box()
