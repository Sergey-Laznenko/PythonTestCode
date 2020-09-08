"""
На вход программе подается строка текста. Напишите программу,
которая определяет является ли введенная строка корректным телефонным номером.
Строка текста является корректным телефонным номером если она имеет формат:

abc-def-hijk или
7-abc-def-hijk

где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
"""

numbers = input().split('-')

if len(numbers) == 4:
    if numbers[0] == '7' and numbers[1].isdigit() and len(numbers[1]) == 3 and numbers[2].isdigit() and len(
            numbers[2]) == 3 and numbers[3].isdigit() and len(numbers[3]) == 4:
        print("YES")
    else:
        print("NO")
elif len(numbers) == 3:
    if (numbers[0].isdigit() and len(numbers[0]) == 3) and (numbers[1].isdigit() and len(numbers[1]) == 3) and (
            numbers[2].isdigit() and len(numbers[2]) == 4):
        print("YES")
    else:
        print("NO")

else:
    print("NO")