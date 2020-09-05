"""
Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и
возвращающую количество делителей данного числа.
"""


# 1 вариант
def get_factors(num):
    score = 0
    for i in range(1, num + 1):
        if num % i == 0:
            score += 1
    return score


n = int(input())
print(get_factors(n))


# 2 вариант
def get_factors(num):
    return len([i for i in range(1, num + 1) if num % i == 0])


n = int(input())
print(get_factors(n))
