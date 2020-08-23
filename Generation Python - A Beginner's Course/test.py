n = int(input())
count = 0
x = 1

for i in range(1, n + 1):
    for j in range(1, i):
        if i % j == 0:
            count += 1
        x += 1
    print(i, '+' * count, sep='')
