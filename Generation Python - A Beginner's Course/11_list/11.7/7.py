"""
На вход программе подается натуральное число nnn. Напишите программу, использующую списочное выражение,
которая создает список содержащий квадраты чисел от 1 до n, а затем выводит его элементы построчно,
то есть каждый на отдельной строке.
Для вывода элементов списка используйте цикл for.
"""
n = int(input())
numbers = [i ** 2 for i in range(1, n + 1)]
for i in numbers:
    print(i)
