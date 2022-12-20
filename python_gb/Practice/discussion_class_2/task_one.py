# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81
from os import *
from random import *

system('cls')
print()
num = int(input("Enter a value: "))

for _ in range(num):
    print(randrange(-100, 100), end=", ")





