# Напишите программу,
# которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from my_function import fill_array


def multiply_couples(old_block):
    new_list = []
    for i in range(0, (len(old_block) // 2) + 1):
        new_list.append(old_block[i] * old_block[len(old_block) - i - 1])
    return new_list


number = int(input("Enter amount of elements in a list: "))
my_list = []
print(f'\nThe filled list is {fill_array(number, my_list)}.')
print(multiply_couples(my_list))

    