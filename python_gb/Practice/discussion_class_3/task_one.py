# 1. Реализуйте алгоритм задания случайных чисел
# без использования встроенного генератора
# псевдослучайных чисел.

from time import *

random_number = time()

print(random_number)
print(int(round(random_number % 1 * 1000, 0)))


