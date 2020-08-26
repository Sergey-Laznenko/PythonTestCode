"""
На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу,
которая выводит k-ую букву из введенных строк на одной строке без пробелов.
"""

n = int(input())
data = []
for _ in range(n):
    data.append(input())
num = int(input())
for item in data:
    if len(item) >= num:
        print(item[num - 1], end='')
