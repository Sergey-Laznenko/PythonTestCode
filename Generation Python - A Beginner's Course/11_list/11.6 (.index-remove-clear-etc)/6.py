"""
На вход программе подается строка текста, содержащая различные натуральные числа.
Из данной строки формируется список чисел. Напишите программу, которая меняет местами минимальный и
максимальный элемент этого списка.
"""


# 1 Вариант

data = [int(i) for i in input().split()]
max_in = data.index(max(data))
min_in = data.index(min(data))
data[max_in], data[min_in] = data[min_in], data[max_in]
print(*data)

# 2 Вариант

data = [int(s) for s in input().split()]
max_index, min_index = 0, 0
for i in range(1, len(data)):
    if data[i] > data[max_index]:
        max_index = i
    if data[i] < data[min_index]:
        min_index = i
data[min_index], data[max_index] = data[max_index], data[min_index]
print(' '.join([str(i) for i in data]))
