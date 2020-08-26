"""
Напишите программу, выводящую следующий список:
['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
"""

abc = 'abcdefghijklmnopqrstuvwxyz'
score = 1
data = []
for i in abc:
    data.append(i * score)
    score += 1
print(data)



# 2 вариант

"""
data = []
for i in range(97, 123):
    data.append(chr(i) * (i - 96))
print(data)
"""