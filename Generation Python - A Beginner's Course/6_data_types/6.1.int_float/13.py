"""
Напишите программу, которая упорядочивает три числа от большего к меньшему.
"""

a, b, c = int(input()), int(input()), int(input())
s = (a, b, c)
x = (a + b + c)

print(max(s))
print(abs(x - (max(s) + min(s))))
print(min(s))
