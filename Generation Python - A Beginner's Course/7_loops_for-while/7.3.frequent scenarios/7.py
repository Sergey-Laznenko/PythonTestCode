
# Асимптотическое приближение


from math import log
n = int(input())
count = 0
for i in range(1, n + 1):
    x = 1 / i
    count += x
print(count - log(n))
