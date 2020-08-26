"""
На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
"""

n = int(input())
max_total = 0
total = 0
for _ in range(n):
    num = int(input())
    if num >= max_total:
        total = max_total
        max_total = num
    elif num > total:
        total = num
print(max_total)
print(total)
