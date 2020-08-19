"""
Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево,
к тому же ведьмак не принимает купюры, он принимает только чеканные монеты.
В мире ведьмака существуют монеты с номиналами 1, 5, 10, 25
"""

# Решение через 4 переменные
a = int(input())
count_25 = -1
count_10 = -1
count_5 = -1
count_1 = -1

while count_25 < 0:
    count_25 = (a // 25)

while count_10 < 0:
    count_10 = (a - 25 * count_25) // 10

while count_5 < 0:
    count_5 = (a - (25 * count_25) - (10 * count_10)) // 5

while count_1 < 0:
    count_1 = (a - (25 * count_25) - (10 * count_10) - (5 * count_5) // 1)

print(abs(count_25 + count_10 + count_5 + count_1))


# Решение через 1 переменную
"""
n = int(input())
total = 0
while n >= 25:
    total += 1
    n -= 25
while n >= 10:
    total += 1
    n -= 10
while n >= 5:
    total += 1
    n -= 5
while n >= 1:
    total += 1
    n -= 1
print(total)
"""