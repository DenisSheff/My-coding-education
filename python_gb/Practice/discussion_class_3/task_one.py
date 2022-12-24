# 1. Реализуйте алгоритм задания случайных чисел
# без использования встроенного генератора
# псевдослучайных чисел.

from time import *
from math import *

random_number = time()

print(random_number)
print(int(round(random_number % 1 * 1000, 0)))

def square(a):
    return a * 2


def rect(a, b):
    return a * b


def circle(r):
    return pi * pow(r, 2)


