# 2. Задайте список.
# Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
from random import randint


def fill_list(num_1, num_2, new_block):
    if num_2 > num_1:
        for i in range(num_1, num_2 + 1):
            new_block.append(str(i))
        print(f"The list of numbers in range {number_one} and {number_two} is {new_block}.")
    else:
        print("Error of values.")

number_one = randint(-100, 100)
number_two = randint(-100, 100)
my_list = []

fill_list(number_one, number_two, my_list)
number = input("Enter a value for number: ")
if number in my_list:
    print(f'There is a number {number} in the list.')
else:
    print('Enter different number.')


