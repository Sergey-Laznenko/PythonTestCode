"""
Напишите функцию get_month(language, number), которая принимает на вход два аргумента language – язык ru или en
и number – номер месяца (от 1 до 12) и возвращает название месяца на русском или английском языке.
"""


def get_month(language, number):
    if language == "ru":
        return ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
                'ноябрь',
                'декабрь'][number - 1]

    if language == "en":
        return ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                'november', 'december'][number - 1]


lan = input()
num = int(input())


print(get_month(lan, num))