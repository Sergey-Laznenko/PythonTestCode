"""
Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки.
Напишите программу проверяющую корректность email адреса.
"""

a = input()
print('YES' if '@' in a and '.' in a else 'NO')
