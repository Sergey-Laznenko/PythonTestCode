"""
На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу,
которая для каждого из введенного числа xx выводит значение функции f(x) = x**2 + 2x + 1, каждое на отдельной строке.
"""

n = int(input())
numbers = []
for _ in range(n):
    x = int(input())
    numbers.append(x)
print(*numbers, sep='\n')
print()
result = []
for i in numbers:
    num = i ** 2 + 2 * i + 1
    result.append(num)
print(*result, sep='\n')
