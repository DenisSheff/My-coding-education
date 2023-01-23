# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint


 def fill_array(elements, my_block):
     for _ in range(elements):
         my_block.append(randint(-elements, elements))
     return my_block


def multiply_odds(new_block):
    index_counter = 0
    for i in range(len(new_block)):
        if i % 2 != 0:
            index_counter = index_counter + new_block[i]
    return index_counter


number = int(input("Enter amount of elements in a list: "))
my_list = []
print(f'\nThe filled list is {fill_array(number, my_list)}.\nThe sum of the odd elements is {multiply_odds(my_list)}.')
