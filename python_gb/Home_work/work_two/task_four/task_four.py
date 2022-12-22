# 4.   Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import *


def fill_list(num, new_block):
    for _ in range(num):
        new_block.append((randint(-num, num)))
    return new_block


number = int(input("Enter a value: "))
my_list = []
fill_list(number, my_list)
print(my_list)

file = open('file.txt', 'w')
for i in range(number - 1):
    file.write(input("Enter index value: ") + '\n')  # В случае если нам нужно меньше индексов просто нажать enter
file.close()

file = open('file.txt', 'r')
print(file.read())
file.close()

index_mult = 1
file = open('file.txt', 'r')
file_int = int(float(file.readline()))
for line in file:
    index_mult *= my_list[file_int]
file.close()
print(index_mult)
