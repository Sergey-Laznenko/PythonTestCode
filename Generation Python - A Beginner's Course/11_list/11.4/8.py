"""
На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу,
которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа,
каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.
"""

negatives = []
zeros = []
positives = []

for _ in range(int(input())):
    num = int(input())
    if num < 0:
        negatives.append(num)
    elif num == 0:
        zeros.append(num)
    elif num > 0:
        positives.append(num)

print(*negatives, sep='\n')
print(*zeros, sep='\n')
print(*positives, sep='\n')
