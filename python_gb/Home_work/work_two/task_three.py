# 3. Задайте список из n чисел последовательности (1 + (1/n))^n
# и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06
from math import *

number = int(input("Enter a value: "))
my_list = []
for i in range(1, number + 1):
    my_list.append([i, round(pow(1 + (1 / i), i), 2)])
print(f'Sequence of numbers is {dict(my_list)}.')
