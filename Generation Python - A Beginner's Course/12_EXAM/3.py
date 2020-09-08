"""
На вход программе подается строка текста, содержащая натуральные числа. Напишите программу,
которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.
"""


# 1 Вариант
text = input().split()

total = 0
for i in text:
    total += int(i)
new_text = '+'.join(text)
print(f'{new_text}={total}')

# 2 Вариант
st = input().split()
print('+'.join(st), sum(int(i) for i in st), sep='=')