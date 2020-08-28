"""
На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой. Напишите программу,
которая определяет является ли введенная строка текста корректным ip-адресом.

Программа должна вывести «ДА», если введеная строка является корректным ip-адресом, и «НЕТ» — в противном случае.
"""


answer = 'ДА'
for i in input().split('.'):
    if 0 <= int(i) <= 255:
        answer = 'ДА'
    else:
        answer = 'НЕТ'
        break
print(answer)
