"""
Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
"""

count = 1
for _ in range(10):
    num = int(input())
    if num > 0:
        count *= num
print(count)
