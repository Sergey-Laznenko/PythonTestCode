"""
Надо написать функцию, которая на входе принимает два аргумента: строку и символ, и возвращает список,
содержащий все индексы данного символа в строке.
"""


# 1 решение --------------------

def find_all(target, symbol):
    data = []
    if symbol in target:
        for i in range(len(target)):
            if target[i] == symbol:
                data.append(i)
    return data


s = input()
char = input()

print(find_all(s, char), end=' ')


# 2 Решение enumerate --------------------

def find_all(target, symbol):
    ind_str = []
    for index, value in enumerate(target):
        if value == symbol:
            ind_str.append(index)
    return ind_str


s = input()
char = input()

print(find_all(s, char))


# 3 решение списочные выражения -----------

def find_all(target, symbol):
    return [idx for idx, c in enumerate(target) if c == symbol]


s = input()
char = input()

print(find_all(s, char))
