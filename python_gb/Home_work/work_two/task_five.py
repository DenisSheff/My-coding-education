# Реализуйте алгоритм перемешивания списка.
from random import *

number = int(input("Enter an amount of elements in the list: "))
new_list = []

for i in range(number):
    new_list.append(randint(-100, 100))

print(f"Original list is {new_list}.")
# shuffle(new_list)
# print(f"Shuffled list is {new_list}.")
for _ in range(number):  # Выдает более рандомные значения при перемешевании элемента
    shuffle(new_list)
print(f"Shuffled list is {new_list}.")
