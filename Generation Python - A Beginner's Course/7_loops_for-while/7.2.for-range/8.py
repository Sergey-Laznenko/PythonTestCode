"""
Даны два целых числа m и n. Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания,
если m < n, или в порядке убывания в противном случае.
"""

m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)

count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p *= x
        count += 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')