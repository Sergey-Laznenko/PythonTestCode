x = 0
y = 0

n = int(input())

for _ in range(n):
    napr, cnt = input().lower().split()
    cnt = int(cnt)

    if napr == 'север':
        y += cnt
    elif napr == 'юг':
        y -= cnt
    elif napr == 'восток':
        x += cnt
    elif napr == 'запад':
        x -= cnt

print(x, end=' ')
print(y)
