# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import uniform


def fill_array(elements, range_number, new_block):
    for _ in range(elements):
        new_block.append(round(uniform(-range_number, range_number), 2))
    return new_block


number = int(input("Enter a value for list: "))
range_num = int(input("Enter a value for a range: "))
my_list = []

fill_array(number, range_num, my_list)
print(my_list)
print(max(my_list[range_num % 1]) - min(my_list[range_num % 1]))
