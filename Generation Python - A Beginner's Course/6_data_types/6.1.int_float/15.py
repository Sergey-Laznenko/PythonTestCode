"""
На вход программе подается пять действительных чисел a1, a_2, a3, a4, a5, каждое на отдельной строке.
Программа должна вывести одно число – сумму модулей введёных чисел.
"""

a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())
print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))
