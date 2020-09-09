"""
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text,
состоящую из символов ( и ) и возвращает значение True
если поступившая на вход строка является правильной скобочной последовательностью и False в противном случае.
"""


def is_correct_bracket(text):
    meet = 0
    for i in text:
        if i == '(':
            meet += 1
        elif i == ')':
            meet -= 1
        if meet < 0:
            return False

    return meet == 0


txt = input()

print(is_correct_bracket(txt))
