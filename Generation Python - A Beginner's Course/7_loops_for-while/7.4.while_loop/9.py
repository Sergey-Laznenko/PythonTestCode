"""
На вход программе подается последовательность слов, каждое слово на отдельной строке.
Концом последовательности является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек).
Напишите программу, которая выводит члены данной последовательности.
"""

text = input()
while text not in ('КОНЕЦ', 'конец'):
    print(text)
    text = input()
