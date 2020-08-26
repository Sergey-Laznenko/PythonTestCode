"""
Дано натуральное число. Напишите программу, которая вычисляет:

- количество цифр 3 в нем;
- сколько раз в нем встречается последняя цифра;
- количество четных цифр;
- сумму его цифр, больших пяти;
- произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
- сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

"""

num = int(input())

last = num % 10
num3 = 0
score_last = 0
even = 0
over5 = 0
multi_over7 = 1
count_over7 = 0
num_0_5 = 0

while num != 0:
    n = num % 10
    if n == 3:
        num3 += 1
    if n == last:
        score_last += 1
    if n % 2 == 0:
        even += 1
    if n > 5:
        over5 += n
    if n > 7:
        multi_over7 *= n
        count_over7 += 1
    if n == 0 or n == 5:
        num_0_5 += 1
    num //= 10

print(num3)
print(score_last)
print(even)
print(over5)

if count_over7 == 0:
    print(1)
else:
    print(multi_over7)

print(num_0_5)
