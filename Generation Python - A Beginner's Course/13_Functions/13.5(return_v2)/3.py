"""
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое
простое число большее числа num.
"""

from math import sqrt


def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, int(sqrt(n) + 1), 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True


def next_prime(x):
    if x <= 1:
        return 2
    prime = x
    found = False

    while not found:
        prime = prime + 1
        if is_prime(prime):
            found = True

    return prime


n = int(input())
print(next_prime(n))
