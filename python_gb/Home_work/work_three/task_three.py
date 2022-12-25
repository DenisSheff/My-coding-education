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


def find_difference(new_block):
    new_list = []
    for i in new_block:
        if i > 0:
            division_sign = round((i % 1), 2)
        else:
            division_sign = round((i % (-1)), 2)
        new_list.append(division_sign)
    max_element = max(new_list)
    min_element = min(new_list)
    print(max_element - min_element)


number = int(input("Enter an amount of elements in a list: "))
range_num = int(input("Enter a value for a elements range: "))
my_list = []

fill_array(number, range_num, my_list)
print(my_list)
find_difference(my_list)
