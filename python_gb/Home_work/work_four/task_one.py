# 1. Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.$    10^-1 <= d <= 10^-10

from math import pi

d = int(input("Enter a value to set numbers after comma sign for Pi: "))
print(f'Pi wi amount numbers {d} after comma is {round(pi, d)}.')
