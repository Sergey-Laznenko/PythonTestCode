"""
На вход программе подается натуральное число n ≥ 2, а затем n целых чисел.
Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел
"""

n = int(input())
data = []
for _ in range(1, n + 1):
    num = int(input())
    data.append(num)
result = []
score = 0
while len(data) != 1:
    a = data[0] + data[1]
    result.append(a)
    del data[0]
print(result)
