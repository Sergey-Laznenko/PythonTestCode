"""
Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка,
состоящих из целых чисел, и объединяет их в один отсортированный список.
"""


def merge(list1, list2):
    return sorted(list1 + list2)


numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))
