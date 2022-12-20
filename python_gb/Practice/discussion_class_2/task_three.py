# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

from os import *
system('cls')

str_1 = input("Enter value of the first string: ")
str_2 = input("Enter value of the second string: ")

# counter = str_1.lower().count(str_2.lower())
# print(counter)

# print(str_1.lower().count(str_2.lower()))
# метод count() является встроенным методом строки который считает количество вхождений в строку

counter = 0
for i in range(len(str_1) - len(str_2)):  # проходим по всей строке по индексам
    if str_2 != str_1[i: i + len(str_2)]:  # если они не равны
        counter += 1
print(f"Second string is located in the first one {counter} times.")
