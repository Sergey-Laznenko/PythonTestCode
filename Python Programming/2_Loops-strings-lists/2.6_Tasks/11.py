"""
Выведите таблицу размером n×n, заполненную числами от 1 до n**2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
"""

n = int(input())
dx, dy = 0, 1
x, y = 0, 0
arr = [[0] * n for i in range(n)]
for i in range(1, n**2 + 1):
    arr[x][y] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n:
        if arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            dx, dy = dy, -dx
            x, y = x + dx, y + dy
    else:
        dx, dy = dy, -dx
        x, y = x + dx, y + dy
for i in range(len(arr)):
    print(*arr[i])
