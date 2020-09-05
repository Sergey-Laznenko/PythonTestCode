"""
Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах
и возвращает расстояние в милях.
"""


def convert_to_miles(km):
    return km * 0.6214


num = int(input())
print(convert_to_miles(num))
