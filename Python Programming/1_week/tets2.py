a, b, c, = len(input()), len(input()), len(input())

d = ((2 * b - c - a)*(2 * c - b - a)*(2 * a - b - c))
if d == 0:
    print('YES')
else:
    print('NO')