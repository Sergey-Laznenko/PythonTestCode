"""
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
"""


# 1
def print_digit_sum(_):
    print(sum([int(num) for num in str(n)]))


n = int(input())
print_digit_sum(n)


# 2
def print_digit_sum(num):
    result = 0
    while num != 0:
        n = num % 10
        result += n
        num //= 10
    print(result)


n = int(input())

print_digit_sum(n)
