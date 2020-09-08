l = input().split()
m = input().split()

for num, _ in enumerate(l):
    print(str(int(l[num]) + int(m[num])), end=' ')


l = input().split()
m = input().split()

for i in range(len(l)):
    print(int(l[i]) + int(m[i]), end=' ')
