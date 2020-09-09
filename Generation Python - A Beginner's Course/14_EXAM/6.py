"""
Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа n и k,
и возвращает значение биномиального коэффициента, равного n! / k!*(n-k)!
"""


def factorial(num):
    if num == 0 or num == 1:
        return 1
    return factorial(num - 1) * num


def compute_binom(x, y):
    return factorial(x) / (factorial(y) * factorial(x - y))


n = int(input())
k = int(input())

print(int(compute_binom(n, k)))
