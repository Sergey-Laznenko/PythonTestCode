"""
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре»
и преобразует его в «змеиный регистр».
"""


def convert_to_python_case(text, sep='_'):
    snake_register = ''
    for i in text:
        if i.isupper():
            snake_register += sep + i.lower()
        else:
            snake_register += i
    return snake_register.lstrip(sep)


txt = input()

print(convert_to_python_case(txt))
