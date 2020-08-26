"""
На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы
"""

n = int(input())
even = 0
odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print(odd - even)
