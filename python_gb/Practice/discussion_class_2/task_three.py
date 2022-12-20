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
    flag = False
    if str_2[0] == str_1[i]:  # если находим соответствие то проверяем
        flag = True
        for j in range(1, len(str_2)):  # проверяем вторую строку
            if str_2[j] != str_1[i + j]:  # если они не равны
                flag = False
        if flag:
            counter += 1
print(f"Second string is located in the first one {counter} times.")