"""
На вход программе подается два натуральных числа a и b (a < b). Напишите программу,
которая находит все простые числа от a до b включительно.
"""
# Пока нет решения
"""
a, b = int(input()), int(input())
lst = []
k = 0
for i in range(2, b + 1):
    for j in range(2, i):
        if i % j == 0:
            k = k + 1
    if k == 0:
        lst.append(i)
    else:
        k = 0
print(*lst, sep='\n')



n = int(input())

lst = []
k = 0
for i in range(2, n + 1):
    for j in range(2, i):

        if i % j == 0:
            k = k + 1

    if k == 0:
        lst.append(i)
    else:
        k = 0

print(lst)
"""
"""
a, b = map(int, input().split())
ls = []
for i in range(a, b + 1):
    if all(i % n != 0 for n in range(2, i)):
        ls.append(str(i))
if len(ls):
    print(' '.join(ls))
else:
    print(0)
"""

a, b = int(input()), int(input())
for i in range(a, b + 1,):
    for j in range(1, i+1,):
        if i > 1 and j == 1 or j == i:
            print(i)
