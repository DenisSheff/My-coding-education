# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

from os import *
system('cls')

str_1 = input("Enter value of the first string: ")
str_2 = input("Enter value of the second string: ")

# count = str_1.lower().count(str_2.lower())

# print(count)

print(str_1.lower().count(str_2.lower()))
# метод count() является встроенным методом строки который считает количество вхождений в строку