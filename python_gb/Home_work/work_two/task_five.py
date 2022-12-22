# Реализуйте алгоритм перемешивания списка.
from random import *

number = int(input("Enter an amount of elements in the list: "))
new_list = []

for i in range(number):
    new_list.append(randint(-number, number))

print(f"Original list is {new_list}.")
# shuffle(new_list)
# print(f"Shuffled list is {new_list}.")

# Выдает более рандомные значения при перемешевании элемента
# Через встроенную функцию
# for _ in range(number):
#     shuffle(new_list)
# print(f"Shuffled list is {new_list}.")

for element in range(number - 1):
    i = randint(-number, number)
    new_list[i], new_list[element] = new_list[element], new_list[i]
print(new_list)