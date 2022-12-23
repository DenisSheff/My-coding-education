# Напишите программу,
# которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import *


def fill_array(elements, new_block):
    for _ in range(elements):
        new_block.append(randint(-elements, elements))
    return new_block

number = int(input("Enter amount of elements in a list: "))
new_list = []
print(f'\nThe filled list is {fill_array(number, new_list)}.')


def multiply_couples(new_block):
    