# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint


def fill_array(elements, new_block):
    for _ in range(elements):
        new_block.append(randint(-elements, elements))
    return new_block

def find_identical(old_block):
    new_block = []
    for element in old_block:
        if element not in new_block:
            new_block.append(element)
    return new_block


amount_elements = int(input("Enter amount of numbers in a list: "))
my_list = []
print(f'Created list: {fill_array(amount_elements, my_list)}.')
print(f'List withour repeated number: {find_identical(my_list)}.')

