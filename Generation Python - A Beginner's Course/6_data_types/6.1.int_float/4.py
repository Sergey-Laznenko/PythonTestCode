"""
Два автомобиля едут навстречу друг другу с постоянными скоростями V1 и V2 км/ч.
Определите, через какое время автомобили встретятся, если расстояние между ними равно S км.
"""

s, v1, v2 = float(input()), float(input()), float(input())
print(s / (v1 + v2))