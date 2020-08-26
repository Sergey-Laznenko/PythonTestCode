"""
На вход программе подается строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
"""

text = input()
text = text[::-1]
most_common = second = 0

for item in text:
    qty = text.count(item)
    if qty > second:
        second = qty
        most_common = item
print(most_common)
