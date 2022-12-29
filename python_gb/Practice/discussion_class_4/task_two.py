# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#
#     1) с помощью математических формул нахождения корней квадратного уравнения
#
#     2) с помощью дополнительных библиотек Python
#
from math import *


a = int(input("Enter a value for 'A': "))
b = int(input("Enter a value for 'B': "))
c = int(input("Enter a value for 'C': "))
x_1 = 0
x_2 = 0

d = pow(b, 2) - 4 * a * c
if d < 0:
    print("There are no math roots.")
elif d == 0:
    print(-b / (2 * a))
else:
    x_1 = (-b + sqrt(d)) / (2 * a)
    x_2 = (-b - sqrt(d)) / (2 * a)
    print(x_1, x_2)
