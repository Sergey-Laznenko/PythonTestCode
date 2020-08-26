"""
Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
"""

from math import *

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(sqrt((x1 - x2)**2 + (y1 - y2)**2))
