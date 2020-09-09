"""
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text,
состоящую из символов ( и ) и возвращает значение True
если поступившая на вход строка является правильной скобочной последовательностью и False в противном случае.
"""


def is_correct_bracket(s):
    meetings = 0
    for c in s:
        if c == '(':
            meetings += 1
        elif c == ')':
            meetings -= 1
        if meetings < 0:
            return False

    return meetings == 0


txt = input()

print(is_correct_bracket(txt))
